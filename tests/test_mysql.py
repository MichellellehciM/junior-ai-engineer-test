import mysql.connector
from dotenv import load_dotenv
import os

# 載入 .env 文件
load_dotenv()

def connect_to_database():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection


# 蒐集退貨資訊
def collect_return_info():
    print("您好，我是AI小幫手，請提供以下資訊以處理您的退貨申請：")
    name = input("請輸入您的大名：")
    phone = input("請輸入您的聯絡電話：")
    order_number = input("請輸入您的訂單單號：")
    product_name = input("請輸入您要退貨的商品名稱：")
    reason = input("請簡單說明退貨的原因：")
    return name, phone, order_number, product_name, reason

# 插入數據到資料庫
def insert_return_request(name, phone, order_number, product_name, reason):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = """
        INSERT INTO returns (name, phone, order_number, product_name, reason)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, phone, order_number, product_name, reason))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"感謝您的資訊，{name}！您的退貨請求已提交，我們的客服團隊會在1-2個工作日內與您聯繫。")


# 主函式
def main():
    # 蒐集資料
    name, phone, order_number, product_name, reason = collect_return_info()
    
    # 確認資訊
    print(f"""
    請確認您的退貨資訊：
    姓名: {name}
    電話: {phone}
    訂單號: {order_number}
    商品名稱: {product_name}
    退貨理由: {reason}
    """)
    confirmation = input("請回覆 '確認' 以提交退貨申請，或輸入 'n' 再次輸入資訊：")
    
    if confirmation == "Y":
        insert_return_request(name, phone, order_number, product_name, reason)
    else:
        print("請重新提供退貨資訊。")
        main()

# 只有當此程式被直接執行時，main() 才會執行。
if __name__ == "__main__":
    main()
