# 此檔案負責 MySQL 連線 與 插入資料

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    """ 連接 MySQL """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def insert_return_request(name, phone, order_number, product_name, reason):
    """ 插入退貨申請資料 """
    if not all([name.strip(), phone.strip(), order_number.strip(), product_name.strip(), reason.strip()]):
        raise ValueError("❌ 所有欄位都必須填寫，請檢查您的輸入！")
    
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
