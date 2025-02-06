from quick_replies.quick_replies import generate_quick_replies, clean_chat_history, clean_list


# test_data 1
# 1. 對話紀錄設計（包含髒數據）
chat_history = [
    {"role": "system", "content": "歡迎來到 JTCG Shop，這裡是系統訊息"},  # 無效的系統訊息
    {"role": "assistant", "content": [{"type": "text", "text": "您好！歡迎來到 JTCG Shop，有什麼我可以為您服務的？"}]},           
    {"role": "user", "content": "我要送禮給女生要選啥"},
    {"role": "unknown", "content": "這是無效的角色"},  # 無效的角色
    {"role": "assistant", "content": None},  # 髒數據，缺少內容
    {"role": "user", "content": "請問有沒有高級香氛產品？"},  
    {"role": "assistant", "content": "我們有【Inner hows】高奢香氛沐浴油，但目前庫存緊張！"},
    {"role": "user", "content": "能推薦幾款適合送禮的嗎？"},
    {"role": "assistant", "content": ""},
    {"role": "user", "content": "那有沒有價格比較優惠的產品？"},
    {"role": "assistant", "content": "這些都是近期的熱賣商品：素色T桖、Macbook Pro、日本A5和牛-3。"}
]

# 2. 髒資料清理
cleaned_data = clean_chat_history(chat_history)
print(cleaned_data)

# 3. 定義 FAQ 列表 & product 列表
faq_list = [
    "111", 
    "如何成為會員",
    "如何取得優惠券",
    "如何退貨",
    "如何追蹤訂單狀態"
]
product_list = [
    "ipad 0 元",                           
    "Macbook Pro",                         
    "日本A5和牛-3",                        
    "3合1電眼睫毛膏",                      
    "【Inner hows】高奢香氛沐浴油250109",                                             
    "休閒百搭帆布包",                      
    "全新盒裝四色懶人實用珠光霧面閃鑽亮粉彩妝眼影",                                   
    "素色T桖",                             
    "素色 V 領小可愛",                     
    "高效保濕"  
]

# 4. FAQ 和 product list 清理 
cleaned_faq_list = clean_list(faq_list)
cleaned_product_list = clean_list(product_list)

# 5. 生成 Quick Replies
quick_replies = generate_quick_replies(cleaned_data, cleaned_faq_list, cleaned_product_list)
print(quick_replies)








# 測試OpenAI API
# print(f"API Key: {os.environ.get('OPENAI_API_KEY')}")