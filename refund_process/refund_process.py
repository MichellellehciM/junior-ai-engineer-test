import mysql.connector
from dotenv import load_dotenv
import os

# 載入 .env 文件
load_dotenv()

# 1. 連接資料庫
def connect_to_database():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection


# 2. 逐步詢問使用者資訊
def collect_return_info():
    """逐步詢問使用者，收集完整退貨資訊"""
    print("您好，我是AI小幫手，請提供以下資訊以處理您的退貨申請：")
    name = input("請輸入您的大名：")
    phone = input("請輸入您的聯絡電話：")
    order_number = input("請輸入您的訂單單號：")
    product_name = input("請輸入您要退貨的商品名稱：")
    reason = input("請簡單說明退貨的原因（如：商品損壞、尺寸不合）：")
    return name, phone, order_number, product_name, reason

# 3. 插入資料到 MySQL 資料庫
def insert_return_request(name, phone, order_number, product_name, reason):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = """
        INSERT INTO returns (name, phone, order_number, product_name, reason)
        VALUES (%s, %s, %s, %s, %s)
    """
    # 執行 SQL 語句
    cursor.execute(query, (name, phone, order_number, product_name, reason))
    # 提交事務
    connection.commit()
    print(f"感謝您的資訊！{name}，您的退貨請求已提交，我們的客服團隊會在1-2個工作日內與您聯繫。")
    # 關閉連線
    cursor.close()
    # 關閉資料庫連線
    connection.close()
   


#  4. 主執行流程
def main():
    """執行退貨流程"""
    name, phone, order_number, product_name, reason = collect_return_info()
    
    # 確認資訊
    print(f"""
    請確認您的退貨資訊：
    姓名: {name}
    電話: {phone}
    訂單單號: {order_number}
    商品名稱: {product_name}
    退貨理由: {reason}
    """)
    confirmation = input("請回覆 'y' 以提交退貨申請，或輸入 'n' 再次輸入資訊：")
    
    if confirmation == 'y':
        insert_return_request(name, phone, order_number, product_name, reason)
    else:
        print("退貨申請取消，請重新提供退貨資訊。")
        main()

# 只有當此程式被直接執行時，main() 才會執行。
if __name__ == "__main__":
    main()
