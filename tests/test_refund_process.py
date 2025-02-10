import unittest
from refund_process import insert_return_request, connect_to_database

class TestRefundProcess(unittest.TestCase):
    # 1. 測試資料庫連線
    def setUp(self):
        """在每個測試前執行：建立測試用的資料庫連線"""
        self.connection = connect_to_database()
        self.cursor = self.connection.cursor()

        # 建立測試資料表（如果尚未存在）
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS returns (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone VARCHAR(20) NOT NULL,
                order_number VARCHAR(50) NOT NULL,
                product_name VARCHAR(255) NOT NULL,
                reason TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.connection.commit()
    # 測試資料庫連線
    def tearDown(self):
        """在每個測試後執行：清理測試資料"""
        self.cursor.execute("DELETE FROM returns")  # 刪除所有測試資料
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    # 2. 測試成功插入退貨資訊
    def test_insert_valid_return_request(self):
        """測試：插入有效的退貨請求"""
        insert_return_request("Alice", "1234567890", "ORD123", "Laptop", "Product defect")
        self.cursor.execute("SELECT * FROM returns WHERE order_number='ORD123'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Alice")  # 驗證姓名是否正確
        self.assertEqual(result[2], "1234567890")  # 驗證電話是否正確
        self.assertEqual(result[3], "ORD123")  # 驗證訂單編號是否正確
        self.assertEqual(result[4], "Laptop")  # 驗證退貨商品是否正確
        self.assertEqual(result[5], "Product defect")  # 驗證退貨理由是否正確
    # 3. 測試成功插入退貨資訊
    def test_insert_missing_fields(self):
        """測試：插入缺少欄位的退貨請求，應該引發錯誤"""
        with self.assertRaises(Exception):
            insert_return_request("Bob", "0987654321", "", "Phone", "Changed my mind")
# 4. 測試成功插入退貨資訊
if __name__ == "__main__":
    unittest.main()
