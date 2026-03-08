import csv
import os

class ALPHeader:
    def __init__(self,raw:list):
        self.raw_data = raw
        try:
            self.name = raw[0].split('：')[1]
            self.account = raw[1].split('：')[1]
            temp_1 = raw[2].split('\t')
            self.time_start = temp_1[0].split('：')[1].strip('[]')
            self.time_end = temp_1[1].split('：')[1].strip('[]')
            self.export_category = raw[3].split('：')[1].strip('[]')
            self.export_time = raw[4].split('：')[1].strip('[]')
            self.total_records = raw[5].split('：')[1].strip('共笔记录')
            """
            self.deposit_numb
            self.deposit_amount
            self.expenditure_numb
            self.expenditure_amount
            self.other_number
            self.other_amount
            """     
        except IndexError:
            pass

    def __repr__(self):
        return f"<AlipayHeader Name={self.name} Account={self.account} Data={len(self.raw_data)} keys>"



class ALPTransaction:
    def __init__(self,row:str):
        # Separate value by comma
        row = row.split(',')
        if len(row) != 12:
            pass ### Raise incorrect file error

        self.transaction_time = row[0]          # 交易时间
        self.MCC = row[1]                       # 交易分类
        self.counterparty = row[2]              # 交易对方
        self.counterparty_account = row[3]      # 对方账号
        self.description = row[4]               # 商品说明
        self.deposit_expenditure = row[5]       # 收/支
        self.amount = row[6]                    # 金额
        self.method = row[7]                    # 收/付款方式
        self.status = row[8]                    # 交易状态
        self.transaction_ID = row[9]            # 交易订单号
        self.merchant_transaction_ID = row[10]  # 商家订单号
        self.notes = row[11]                    # 备注

    def __repr__(self):
        return f"<Transaction {self.transaction_time} | {self.MCC} {self.amount} | {self.description}>"


def read_file(file_path:str = None)->bool|list:
    lines = []
    # Handle standard Chinese encodings
    encodings = ['gb18030', 'gbk', 'utf-8', 'gb2312']
    decoded = False

    # Try listed encodings
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                lines = f.readlines()
            decoded = True
            break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Error reading file: {e}") ### Output error message
            break
    
    # Return status code and any content
    if decoded:
        return (True, lines)
    else:
        print("Failed to decode file with standard encodings (GBK/UTF-8).")
        return (False, lines)



def process_file(lines)->ALPHeader|list[ALPTransaction]:
    header = None
    lines_header = []
    transactions = []
    reach_header_start = False
    reach_header_end = False
    is_bill_section = False

    for line in lines:
        # 1. Find where file header starts
        if not reach_header_start:
            # Check if header started
            if line.startswith("导出信息"):
                reach_header_start = True
        
        # 2. Add header lines
        elif reach_header_start and (not reach_header_end):
            # Check if reach end of header content by '\n'
            if line == '\n':
                reach_header_end = True
                # Process header
                if len(lines_header) == 9:
                    header = ALPHeader(lines_header)
                else:
                    ### Raise incorrec format
                    pass
            else:
                lines_header.append(line)

        # 3. Check if the transactions started
        elif reach_header_start and reach_header_end and (not is_bill_section):
            if line.startswith("交易时间"):
                is_bill_section = True
        
        # 4.Extract transactions here
        elif is_bill_section:
            if line == '\n':
                break
            transactions.append(ALPTransaction(line))
    
    ### Process empty files here
    if is_bill_section:
        if len(transactions) == 0:
            ### Raise empty file error
            pass
        return header,transactions
    elif reach_header_start and reach_header_end and (not is_bill_section):
        pass



if __name__ == "__main__":
    file_path = '支付宝交易明细(20251101-20251201).csv'
    
    ### Check file name is correct
    if os.path.exists(file_path):
        status_code,file_content = read_file(file_path)
        if status_code:
            header,transactions = process_file(file_content)
            print(header)
            print(transactions)
    else:
        print("File not found.")