import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np
import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple, Optional

# ---------------------------
# Configuration & helpers
# ---------------------------
# Language combination for Tesseract - requires installed languages on the system
TESSERACT_LANG = 'eng+chi_sim'
# Tesseract config - OEM 1 (LSTM), PSM 6 (Assume a uniform block of text)
DEFAULT_TESS_CONFIG = r'--oem 1 --psm 6'

# Currency symbol class (expand if needed)
CURRENCY_SYMBOLS = '¥£$€'  # extend as needed
CURRENCY_REGEX = re.compile(r'([¥£$€]|CNY|GBP|USD|RMB)?\s*([0-9\.,]+)')

def normalize_whitespace(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip()

def extract_currency(text: str) -> Optional[Tuple[str, float]]:
    """Find the first currency-like token and return (symbol_or_code, value)."""
    m = CURRENCY_REGEX.search(text)
    if not m:
        return None
    sym, num = m.groups()
    # normalize number: remove commas, handle periods
    num_norm = num.replace(',', '')
    try:
        val = float(num_norm)
    except ValueError:
        # try swapping comma/dot in some locales
        num_alt = num_norm.replace('.', '').replace(',', '.')
        try:
            val = float(num_alt)
        except ValueError:
            return (sym or '', None)
    return (sym or '', val)

# ---------------------------
# Data structures
# ---------------------------
@dataclass
class FieldResult:
    label: str
    raw_text: str
    parsed: Optional[str] = None
    currency: Optional[Dict] = None

@dataclass
class OCRResult:
    image_path: str
    fields: Dict[str, FieldResult]

    def to_dict(self):
        return {'image_path': self.image_path, 'fields': {k: asdict(v) for k, v in self.fields.items()}}

# ---------------------------
# Main OCR processor
# ---------------------------
class OCRProcessor:
    def __init__(self,
                 tesseract_lang: str = TESSERACT_LANG,
                 tess_config: str = DEFAULT_TESS_CONFIG,
                 label_variants: Optional[Dict[str, List[str]]] = None):
        self.lang = tesseract_lang
        self.config = tess_config
        # mapping: canonical field name -> list of label variations (English + Chinese)
        self.label_variants = label_variants or self._default_label_variants()

    def _default_label_variants(self) -> Dict[str, List[str]]:
        return {
            "Card Number": ["Card Number", "卡号", "Card No", "Cardnumber", "CardNumber"],
            "Transaction Time": ["Transaction Time", "交易时间", "Transaction time"],
            "Transaction Category": ["Transaction Category", "交易类别", "Transaction Category"],
            "Category": ["Category", "类别"],
            "Issuing Institution": ["Issuing Institution", "发卡机构", "Issuing Institution"],
            "Acquiring Institution": ["Acquiring Institution", "收单机构", "Acquiring Institution"],
            "Merchant ID": ["Merchant ID", "商户号"],
            "Terminal ID": ["Terminal ID", "终端号"],
            "Batch Number": ["Batch Number", "批次号"],
            "Voucher Number": ["Voucher Number", "凭证号"],
            "Authorization Number": ["Authorization Number", "授权号"],
            "Reference Number": ["Reference Number", "参考号", "Reference Number"],
            "Order amount": ["Order amount", "订单金额", "Order Amount", "Amount"],
            # Add or tweak fields according to your template
        }

    # ---------- Image preprocessing ----------
    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """Basic preprocessing to improve OCR accuracy."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # denoise
        gray = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)
        # increase contrast via CLAHE
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        gray = clahe.apply(gray)
        # optionally threshold (but keep soft for colored backgrounds)
        #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #                           cv2.THRESH_BINARY, 31, 2)
        return gray

    # ---------- locate labels ----------
    def find_label_positions(self, image: np.ndarray) -> Dict[str, Tuple[int,int,int,int]]:
        """
        Run a light OCR to get word boxes, then find approximate bounding box for each label variant.
        Returns map: canonical_label -> bbox (x, y, w, h) referring to the label text bbox.
        """
        pil = Image.fromarray(image)
        data = pytesseract.image_to_data(pil, lang=self.lang, config=self.config, output_type=Output.DICT)

        # build a list of words with their bboxes
        n_boxes = len(data['text'])
        word_boxes = []
        for i in range(n_boxes):
            txt = data['text'][i].strip()
            if not txt:
                continue
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            word_boxes.append({'text': txt, 'bbox': (x, y, w, h)})

        found = {}
        # for each canonical label, search the OCR words for a matching variant (case-insensitive)
        for canonical, variants in self.label_variants.items():
            for v in variants:
                v_norm = v.strip()
                # match tolerant: often OCR splits label words, so search for label tokens sequentially
                # Strategy: find first word that contains part of variant, or match sequence of words.
                for i in range(len(word_boxes)):
                    # check single-word containment
                    if v_norm.lower() in word_boxes[i]['text'].lower() or word_boxes[i]['text'].lower() in v_norm.lower():
                        found[canonical] = word_boxes[i]['bbox']
                        break
                    # try sequence match of up to 3 words
                    for j in range(1, 4):
                        if i + j <= len(word_boxes):
                            concat = ' '.join(wb['text'] for wb in word_boxes[i:i+j])
                            if v_norm.lower() in concat.lower() or concat.lower() in v_norm.lower():
                                # compute bounding box covering sequence
                                xs = [word_boxes[k]['bbox'][0] for k in range(i, i+j)]
                                ys = [word_boxes[k]['bbox'][1] for k in range(i, i+j)]
                                ws = [word_boxes[k]['bbox'][2] for k in range(i, i+j)]
                                hs = [word_boxes[k]['bbox'][3] for k in range(i, i+j)]
                                x_min = min(xs)
                                y_min = min(ys)
                                x_max = max([xs[k-i]+ws[k-i] for k in range(i, i+j)])
                                y_max = max([ys[k-i]+hs[k-i] for k in range(i, i+j)])
                                found[canonical] = (x_min, y_min, x_max - x_min, y_max - y_min)
                                break
                    if canonical in found:
                        break
                if canonical in found:
                    break
            # if not found, continue; caller can decide to fall back to fixed coords
        return found

    # ---------- crop strategy ----------
    def crop_value_region(self, image: np.ndarray, label_bbox: Tuple[int,int,int,int],
                          next_label_bbox: Optional[Tuple[int,int,int,int]] = None,
                          right_margin: int = 40) -> np.ndarray:
        """
        Given a label bbox, crop the area to the right which likely contains the value.
        If next_label_bbox is provided, crop vertically between label and next label (safer).
        """
        h_img, w_img = image.shape[:2]
        x, y, w, h = label_bbox
        # determine vertical span
        top = y
        bottom = y + h
        if next_label_bbox is not None:
            ny, nh = next_label_bbox[1], next_label_bbox[3]
            # ensure cropping down to just above next label
            bottom = max(bottom, ny)  # keep at least the label height
            # but to be safe use midpoint between this label and next label top
            bottom = int((y + (ny)) / 2) if ny > y else bottom

        # horizontal crop: start a bit to the right of the label bbox and go to near right edge
        start_x = x + w + 5
        end_x = w_img - right_margin
        # bounds check
        start_x = min(max(0, start_x), w_img-1)
        end_x = min(max(0, end_x), w_img-1)
        # small safety if start_x >= end_x
        if start_x >= end_x:
            start_x = max(0, x - 120)
            end_x = min(w_img-1, x + w + 400)

        crop = image[top:bottom, start_x:end_x]
        if crop.size == 0:
            # fallback: small rectangle to the right of label
            crop = image[y:y+h, x+w:x+w+200]
        return crop

    # ---------- OCR a crop ----------
    def ocr_crop(self, crop: np.ndarray) -> str:
        if crop is None or crop.size == 0:
            return ""
        pil = Image.fromarray(crop)
        txt = pytesseract.image_to_string(pil, lang=self.lang, config=self.config)
        return normalize_whitespace(txt)

    # ---------- main public API ----------
    def extract_fields(self, image_path: str) -> OCRResult:
        """Given an image path, extract the fields according to the template."""
        img_bgr = cv2.imread(image_path)
        if img_bgr is None:
            raise FileNotFoundError(f"Cannot open image '{image_path}'")
        pre = self.preprocess(img_bgr)

        # find label positions
        labels_bbox = self.find_label_positions(pre)

        # sort labels by vertical position
        sorted_labels = sorted(labels_bbox.items(), key=lambda kv: kv[1][1])

        # build crops and OCR
        results: Dict[str, FieldResult] = {}
        for i, (canonical, bbox) in enumerate(sorted_labels):
            next_bbox = sorted_labels[i+1][1] if (i+1) < len(sorted_labels) else None
            crop = self.crop_value_region(pre, bbox, next_label_bbox=next_bbox)
            raw = self.ocr_crop(crop)
            # postprocess parse currency if found
            currency_info = None
            cur = extract_currency(raw)
            if cur:
                symbol, val = cur
                currency_info = {'symbol_or_code': symbol, 'value': val}

            results[canonical] = FieldResult(label=canonical, raw_text=raw, parsed=None,
                                             currency=currency_info)

        # For labels not found by OCR, create empty FieldResult (optional)
        for canonical in self.label_variants.keys():
            if canonical not in results:
                results[canonical] = FieldResult(label=canonical, raw_text="", parsed=None, currency=None)

        return OCRResult(image_path=image_path, fields=results)

# ---------------------------
# Example usage
# ---------------------------
if __name__ == '__main__':
    import json
    # supply your path
    image_path = 'img/IMG_8770.png'  # change to your file

    processor = OCRProcessor()
    result = processor.extract_fields(image_path)
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
