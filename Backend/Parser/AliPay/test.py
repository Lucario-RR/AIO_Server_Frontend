import csv
import io
import os

class AlipayHeader:
    """
    Stores the header summary information from the Alipay CSV.
    """
    def __init__(self):
        self.raw_data = {}
        self.name = None
        self.account = None
        
    def add_info(self, line):
        line = line.strip()
        if not line:
            return
        
        # Simple parsing logic for key-value pairs (e.g., 姓名：Name)
        if '：' in line:
            try:
                parts = line.split('：', 1)
                key = parts[0].strip()
                value = parts[1].strip()
                self.raw_data[key] = value
                
                if key == '姓名':
                    self.name = value
                elif key == '支付宝账户':
                    self.account = value
            except IndexError:
                pass

    def __repr__(self):
        return f"<AlipayHeader Name={self.name} Account={self.account} Data={len(self.raw_data)} keys>"

class AlipayTransaction:
    """
    Stores individual transaction data.
    """
    def __init__(self, row):
        # Row is expected to be a dictionary from csv.DictReader
        self.raw_row = row
        self.trans_time = row.get('交易时间', '').strip()
        self.category = row.get('交易分类', '').strip()
        self.counterparty = row.get('交易对方', '').strip()
        self.counterparty_account = row.get('对方账号', '').strip()
        self.description = row.get('商品说明', '').strip()
        self.type = row.get('收/支', '').strip()
        
        self.amount = 0.0
        try:
            self.amount = float(row.get('金额', '0').strip())
        except ValueError:
            pass
            
        self.payment_method = row.get('收/付款方式', '').strip()
        self.status = row.get('交易状态', '').strip()
        
        # Order IDs often have trailing tabs/spaces in CSV
        self.order_id = row.get('交易订单号', '').strip()
        self.merchant_order_id = row.get('商家订单号', '').strip()
        self.remark = row.get('备注', '').strip()

    def __repr__(self):
        return f"<Transaction {self.trans_time} | {self.type} {self.amount} | {self.description}>"

class AlipayParser:
    """
    Main class to parse Alipay CSV files.
    """
    def __init__(self):
        self.header_info = AlipayHeader()
        self.transactions = []

    def parse(self, file_path=None, content=None):
        """
        Parses the CSV data.
        :param file_path: Path to the .csv file.
        :param content: Raw string content of the csv.
        """
        lines = []
        
        # 1. Load Content
        if content:
            lines = content.splitlines()
        elif file_path:
            # Handle standard Chinese encodings
            encodings = ['gbk', 'utf-8', 'gb18030', 'gb2312']
            decoded = False
            for enc in encodings:
                try:
                    with open(file_path, 'r', encoding=enc) as f:
                        lines = f.readlines()
                    decoded = True
                    break
                except UnicodeDecodeError:
                    continue
                except Exception as e:
                    print(f"Error reading file: {e}")
                    return
            if not decoded:
                print("Failed to decode file with standard encodings (GBK/UTF-8).")
                return
        else:
            print("Error: No file path or content provided.")
            return

        # 2. Process Lines
        self._process_lines(lines)

    def _process_lines(self, lines):
        """Internal logic to separate header metadata from table data."""
        is_data_section = False
        header_row = None
        data_lines = []

        for line in lines:
            line = line.strip()
            
            # The data section typically starts with the column headers
            if not is_data_section:
                if line.startswith("交易时间"):
                    is_data_section = True
                    header_row = line
                    continue
                
                # Metadata section
                self.header_info.add_info(line)
            else:
                # Data section (skip separator lines)
                if not line or line.startswith("----------------"): 
                    continue
                data_lines.append(line)

        # 3. Parse Data Table
        if header_row and data_lines:
            # Clean header (remove potential trailing comma for proper key mapping)
            clean_header = header_row.strip(',')
            
            # Reconstruct CSV for the standard library parser
            csv_content = [clean_header] + data_lines
            f = io.StringIO('\n'.join(csv_content))
            
            try:
                # specific handling for trailing commas in rows if they exist
                reader = csv.DictReader(f)
                for row in reader:
                    # Filter out empty keys resulting from trailing commas
                    clean_row = {k.strip(): v for k, v in row.items() if k}
                    self.transactions.append(AlipayTransaction(clean_row))
            except csv.Error as e:
                print(f"CSV Parsing Error: {e}")

    # --- Placeholders for Extensions ---

    def save_to_sql(self, connection_string):
        """
        [Placeholder] Logic to save transactions to a SQL database.
        """
        print(f"Connecting to SQL at {connection_string}...")
        # Example:
        # engine = sqlalchemy.create_engine(connection_string)
        # ... logic to insert self.transactions ...
        pass

    def process_data(self):
        """
        [Placeholder] Basic data processing / Analysis.
        """
        if not self.transactions:
            return
            
        total_income = sum(t.amount for t in self.transactions if t.type == '收入')
        total_expense = sum(t.amount for t in self.transactions if t.type == '支出')
        
        print(f"--- Data Processing Summary ---")
        print(f"Total Transactions: {len(self.transactions)}")
        print(f"Calculated Income: {total_income:.2f}")
        print(f"Calculated Expense: {total_expense:.2f}")

# --- Usage Example ---
if __name__ == "__main__":
    # Example usage with the file path
    parser = AlipayParser()
    target_file = '支付宝交易明细(20251101-20251201).csv'
    
    if os.path.exists(target_file):
        print(f"Parsing file: {target_file}")
        parser.parse(file_path=target_file)
        
        print("\n[Header Info]:")
        print(parser.header_info.raw_data)
        
        print(f"\n[Transactions]: Loaded {len(parser.transactions)} items")
        if parser.transactions:
            print(f"First item: {parser.transactions[0]}")
            
        parser.process_data()
    else:
        print("File not found.")