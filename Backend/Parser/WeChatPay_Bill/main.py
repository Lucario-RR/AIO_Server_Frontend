import os
import sys
import openpyxl

class DBManager:
    """
    Placeholder class for handling SQL connections.
    """
    def __init__(self, connection_string: str = None):
        self.connection_string = connection_string
        self.connection = None

    def connect(self):
        """Establish connection to the database."""
        try:
            # Implement SQL connection logic here
            # e.g., self.connection = sqlite3.connect(self.connection_string)
            print("DB Connection established (Mock).") # status code 101
            pass
        except Exception as e:
            print(f"Failed to connect to DB: {e}") # status code 102

    def insert_transactions(self, transactions: list):
        """Insert a list of transactions into the database."""
        if not self.connection:
            return
        # Implement insert logic here
        pass

    def close(self):
        if self.connection:
            # self.connection.close()
            pass


class WCPHeader:
    def __init__(self, raw: list):
        self.raw_data = raw
        self.name = None
        self.account = None
        self.time_start = None
        self.time_end = None
        self.export_category = None
        self.export_time = None
        self.total_records = None
        
        # Process the header content
        # Using a loop to find keys is more robust than hardcoded indices
        try:
            for line in raw:
                line = str(line).strip()
                if not line:
                    continue
                
                if "微信昵称" in line:
                    self.name = line.split('：')[1].strip('[]')
                
                elif "微信号" in line or "账号" in line:
                    # In case account is present (not in current template but handled)
                    try:
                        self.account = line.split('：')[1].strip('[]')
                    except IndexError:
                        pass
                
                elif "起始时间" in line:
                    # Handle "起始时间：[...] 终止时间：[...]"
                    # Split by space or specific separator if needed
                    try:
                        # Assuming format: 起始时间：[...] 终止时间：[...]
                        # Remove "起始时间：" prefix first
                        content = line.replace("起始时间：", "")
                        # Split by " 终止时间："
                        parts = content.split(" 终止时间：")
                        if len(parts) >= 2:
                            self.time_start = parts[0].strip('[]')
                            self.time_end = parts[1].strip('[]')
                    except Exception:
                        pass
                
                elif "导出类型" in line:
                    self.export_category = line.split('：')[1].strip('[]')
                
                elif "导出时间" in line:
                    self.export_time = line.split('：')[1].strip('[]')
                    
                elif "共" in line and "笔记录" in line:
                    # Format like "共190笔记录"
                    temp = line.replace("共", "").replace("笔记录", "")
                    self.total_records = temp
                    
        except Exception as e:
            print(f"Warning: Error parsing header fields: {e}") # status code 103

    def __repr__(self):
        return (f"<WeChatPayHeader Name={self.name} Account={self.account} "
                f"Time={self.time_start}~{self.time_end} Records={self.total_records}>")


class WCPTransaction:
    def __init__(self, row: tuple):
        # Ensure row has enough columns, otherwise pad with None
        safe_row = list(row) + [None] * (11 - len(row))
        
        self.transaction_time = safe_row[0]          # 交易时间
        self.MCC = safe_row[1]                       # 交易分类
        self.counterparty = safe_row[2]              # 交易对方
        self.description = safe_row[3]               # 商品说明
        self.deposit_expenditure = safe_row[4]       # 收/支
        self.amount = safe_row[5]                    # 金额
        self.method = safe_row[6]                    # 收/付款方式
        self.status = safe_row[7]                    # 交易状态
        self.transaction_ID = safe_row[8]            # 交易订单号
        self.merchant_transaction_ID = safe_row[9]   # 商家订单号
        self.notes = safe_row[10]                    # 备注

    def __repr__(self):
        return f"<Transaction {self.transaction_time} | {self.amount} | {self.description}>"


def read_file(file_path: str = None) -> tuple[str, openpyxl.Workbook] | tuple[str, None]:
    # Consider all the posibilities may causing bugs (File types)
    if not os.path.isfile(file_path):
        return ('4021', None)
    
    # Check extension
    if not (file_path.lower().endswith('.xlsx') or file_path.lower().endswith('.xls')):
        return ('4022', None)

    try:
        # Load the workbook and active sheet
        wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
        return ('7024', wb) # Status code 303
    except Exception as e:
        return ('4023', None) # Status code 304


def process_file(worksheet):
    status_code = '8001'
    lines_header = []
    transactions = []
    header_obj = None

    # Loop all the rows
    for row in worksheet.iter_rows(values_only=True):
        first_cell = str(row[0]) if row[0] is not None else ""
        
        # 1. Check template before start
        if status_code == '8001':
            if first_cell == "微信支付账单明细":
                status_code = '8002'
            else:
                continue

        # 2. Start extract header rows
        elif status_code == '8002':
            # Check if reach end of header
            if first_cell == "注：":
                status_code = '8003'
                # Process header here
                header_obj = WCPHeader(lines_header)
                ### Handle error with header processing
            
            # Ignore empty lines
            elif first_cell == "":
                continue
            # Append non empty lines
            else:
                lines_header.append(first_cell)
        
        # 3. Find where bills starts
        elif status_code == '8003':
            if "交易时间" in first_cell:
                # Validate columns count (Expected 11 columns for standard WeChat bill)
                if len(row) == 11: 
                    status_code = '8004'
                else:
                    # Return with error
                    return ("8011",header_obj,transactions) # "Template Error: '交易时间' row found but format is incorrect."

        # 4. Process bills
        elif status_code == '8004':
            # Skip empty lines inside bill section
            if not first_cell:
                continue
            transactions.append(WCPTransaction(row))

    return (status_code, header_obj, transactions) 


if __name__ == "__main__":
    file_path = '微信支付账单流水文件(20251101-20251130).xlsx'

    # Check file name is correct & exists
    if not os.path.exists(file_path):
        status_code = '4D250'
        print(f"File '{file_path}' not found.")
        sys.exit(1)

    status_code, result = read_file(file_path)
    
    if status_code:
        workbook = result
        try:
            if workbook.active is None:
                status_code = '5?101'
                print(f"Excel file has no active sheet.")
                exit()
                
            status_code, header, transactions = process_file(workbook.active)

            if status_code == '8004':
                print("Debug")
                print("--- Header Info ---")
                print(header)
                print(f"\n--- Transactions Parsed: {len(transactions)} ---")
                if len(transactions) > 0:
                    print(f"First transaction: {transactions[0]}")
                else:
                    print("No transactions found")
                
                # SQL Connection usage example
                # db = DBManager("mydb.sqlite")
                # db.connect()
                # db.insert_transactions(transactions)
            
            else:
                print(f"Error code {status_code}")

        except Exception as e:
            # Consider all the posibilities may causing bugs and crashes
            print(f"Critical Error during processing: {e}") # status code 105
        finally:
            workbook.close()
    else:
        print(f"Failed to read file: {result}") # status code 106