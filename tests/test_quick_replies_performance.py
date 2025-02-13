# 生成 50 次 Quick Replies
import unittest
import time
from quick_replies.quick_replies import generate_quick_replies, clean_chat_history, clean_list

class TestQuickRepliesPerformance(unittest.TestCase):
    def setUp(self):
        """ 初始化測試資料 """
        self.chat_history = [
            {"role": "system", "content": "歡迎來到 JTCG Shop，這裡是系統訊息"},  
            {"role": "assistant", "content": [{"type": "text", "text": "您好！歡迎來到 JTCG Shop，有什麼我可以為您服務的？"}]},           
            {"role": "user", "content": "我要送禮給女生要選啥"},
            {"role": "unknown", "content": "這是無效的角色"},  
            {"role": "assistant", "content": None},  
            {"role": "user", "content": "請問有沒有高級香氛產品？"},  
            {"role": "assistant", "content": "我們有【Inner hows】高奢香氛沐浴油，但目前庫存緊張！"},
            {"role": "user", "content": "能推薦幾款適合送禮的嗎？"},
            {"role": "assistant", "content": ""},
            {"role": "user", "content": "那有沒有價格比較優惠的產品？"},
            {"role": "assistant", "content": "這些都是近期的熱賣商品：素色T桖、Macbook Pro、日本A5和牛-3。"}
        ]
        self.faq_list = [
            "如何成為會員",
            "如何取得優惠券",
            "如何退貨",
            "如何追蹤訂單狀態"
        ]

        self.product_list = [
            "ipad 0 元",                           
            "Macbook Pro",                         
            "日本A5和牛-3",                        
            "3合1電眼睫毛膏",                      
            "【Inner hows】高奢香氛沐浴油25109",                                            
            "休閒百搭帆布包",                      
            "全新盒裝四色懶人實用珠光霧面閃鑽亮粉彩妝眼影",                                   
            "素色T桖",                             
            "素色 V 領小可愛",                     
            "高效保濕"  
        ]

    def test_generate_quick_replies_50_times(self):
        """ 測試 50 次生成 Quick Replies 的穩定性與速度，並印出每次的回應 """
        execution_times = []
        num_tests = 50

        for i in range(num_tests):
            start_time = time.time()  
            replies = generate_quick_replies(self.chat_history, self.faq_list, self.product_list)
            end_time = time.time()  
            
            execution_time = end_time - start_time
            execution_times.append(execution_time)


            print(f"\n 測試 {i+1} Quick Replies")
            for j, reply in enumerate(replies, start=1):
                print(f" {reply}")


            self.assertTrue(5 <= len(replies) <= 6, f"測試第 {i+1} 次時，回覆數量錯誤: {len(replies)}")

        avg_time = sum(execution_times) / num_tests
        print(f"\n✅ 50 次測試平均回應時間: {avg_time:.3f} 秒")
        print(f"⏳ 最長回應時間: {max(execution_times):.3f} 秒, 最短回應時間: {min(execution_times):.3f} 秒")

if __name__ == "__main__":
    unittest.main()
