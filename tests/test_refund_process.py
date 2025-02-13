import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from refund_process.database import connect_to_database, insert_return_request
from refund_process.validation import validate_name, validate_phone, validate_order_number
from refund_process.gpt_assistant import generate_refund_prompt

class TestRefundProcess(unittest.TestCase):
    
    # 1. 測試資料庫連線
    def setUp(self):
        """ 在每個測試前執行：建立測試用的資料庫連線 """
        print("\n[測試資料庫連線...ok]")
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

    # def tearDown(self):
    #     """ 在每個測試後執行：清理測試資料 """
    #     print("[刪除測試資料...ok]")
    #     self.cursor.execute("DELETE FROM returns")  
    #     self.connection.commit()
    #     self.cursor.close()
    #     self.connection.close()

    # 2. 測試 GPT 詢問姓名
    def test_generate_prompt_missing_name(self):
        """ 測試：當用戶還沒提供姓名時，AI 應該詢問姓名 """
        print("[✅] 測試 GPT 詢問姓名")
        user_info = {"name": "", "phone": "0912345678", "product_name": "iPhone 15", "order_number": "ORD12345", "reason": ""}
        response = generate_refund_prompt(user_info)
        print("[GPT 回應] →", response)
        self.assertIn("姓名", response)

    # 3. 測試 GPT 詢問訂單單號
    def test_generate_prompt_missing_order_number(self):
        """ 測試：當用戶還沒提供訂單單號時，AI 應該詢問訂單單號 """
        print("[✅] 測試 GPT 詢問訂單單號")
        user_info = {"name": "Alice", "phone": "0912345678", "product_name": "iPhone 15", "order_number": "", "reason": ""}
        response = generate_refund_prompt(user_info)
        print("[GPT 回應] →", response)
        self.assertIn("訂單單號", response)

    # 4. 測試 GPT 詢問電話
    def test_generate_prompt_missing_phone(self):
        """ 測試：當用戶還沒提供電話時，AI 應該詢問電話 """
        print("[✅] 測試 GPT 詢問電話")
        user_info = {"name": "Alice", "phone": "", "product_name": "iPhone 15", "order_number": "ORD12345", "reason": ""}
        response = generate_refund_prompt(user_info)
        print("[GPT 回應] →", response)
        self.assertIn("電話", response)

    # 5. 測試 GPT 詢問商品名稱
    def test_generate_prompt_missing_product_name(self):
        """ 測試：當用戶還沒提供商品名稱時，AI 應該詢問商品名稱 """
        print("[✅] 測試 GPT 詢問商品名稱")
        user_info = {"name": "Alice", "phone": "0912345678", "product_name": "", "order_number": "ORD12345", "reason": ""}
        response = generate_refund_prompt(user_info)
        print("[GPT 回應] →", response)
        self.assertIn("商品名稱", response)

    # 6. 測試插入缺少欄位的退貨請求
    def test_insert_missing_fields(self):
        """ 測試：插入缺少欄位的退貨請求，應該拋出 ValueError """
        try:
            insert_return_request("Bob", "0987654321", "", "Phone", "Changed my mind")
        except ValueError as e:
            print(f"ValueError {e}")  # 印出錯誤訊息，確認是否真的拋出 ValueError
            self.assertTrue("所有欄位都必須填寫" in str(e))  # 確保錯誤訊息正確
        else:
            self.fail("❌ 測試失敗，未拋出 ValueError")  # 如果沒有錯誤，就強制讓測試失敗



    # 7. 測試插入退貨請求
    def test_insert_valid_return_request(self):
        """ 測試：存入有效的退貨請求到 MySQL """
        print("[✅] 測試插入有效的退貨請求")
        insert_return_request("Alice", "0912345678", "ORD12345", "iPhone 15", "商品有瑕疵")
        self.cursor.execute("SELECT * FROM returns WHERE order_number='ORD12345'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)  
        self.assertEqual(result[1], "Alice")  
        self.assertEqual(result[2], "0912345678")  
        self.assertEqual(result[3], "ORD12345")  
        self.assertEqual(result[4], "iPhone 15")  
        self.assertEqual(result[5], "商品有瑕疵")  

if __name__ == "__main__":
    unittest.main(verbosity=2)  # 顯示詳細測試資訊
