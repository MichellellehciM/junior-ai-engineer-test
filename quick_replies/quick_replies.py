import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))  

def generate_quick_replies(chat_history, faq_list, product_list):
    """
    根據對話記錄生成 Quick Replies 和 5 個 user 可能會有的後續問題
    :param chat_history:  User 與助理的對話列表
    :param faq_list: 常見問題列表
    :param product_list: 商品清單
    :return: 一個包含 5 個建議回覆的列表
    """
    # 取得 user 最新的問題
    last_user_message = None
    for message in reversed(chat_history):
        if message["role"] == "user":
            last_user_message = message["content"]
            break

    if not last_user_message:
        return ["(AI客服): 很抱歉，我沒有收到您的問題，請您再說一次哦！"]

    # 設定 Prompt
    prompt = f"""
    你是一個友好且專業的客服助理，根據以下的對話記錄，生成 Quick Replies 回應 user 的最新問題，
    並且根據 User 當前的問題，預測他接下來可能會問的 5 個問題，來幫助他獲得更多資訊。

    對話記錄：
    {chat_history}

    以下是常見問題：
    {faq_list}

    以下是產品清單：
    {product_list}


請以以下格式回覆，讓回應更有親和力，可使用適當的 emoji 來讓對話更生動：

😊 **(AI小幫手)**: [針對當前問題的回應]，回答完後可以想辦法挽留對方在網站上停留的時間, 例如我可以幫你詳細介紹、有需要我再幫你查詢更多資訊嗎？

💡 **(你可能還想問 1)**: [使用者可能會問的後續問題]
🔎 **(你可能還想問 2)**: [使用者可能會問的後續問題]
📦 **(你可能還想問 3)**: [使用者可能會問的後續問題]
🛒 **(你可能還想問 4)**: [使用者可能會問的後續問題]
🎁 **(你可能還想問 5)**: [使用者可能會問的後續問題]

🙋‍♀️ **需要真人客服嗎？** 點這裡👉 【真人客服】 小幫手隨時為您服務！✨

    """

    try:
        # 新版 OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "你是一個友善且專業的客服助理。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.7
        )
        # 獲取回覆內容
        content = response.choices[0].message.content.strip()
        replies = content.split("\n")
        return [reply.lstrip("- ") for reply in replies if reply.strip()]
    except Exception as e:
        print(f"生成 Quick Replies 時發生錯誤：{e}")
        return []


# 髒資料清洗
def clean_chat_history(chat_history):
    """
    清理對話記錄，移除髒資料或修正格式不正確的項目
    :param chat_history: 原始對話記錄 (列表形式)
    :return: 清理後的對話記錄
    """
    cleaned_history = []
    for message in chat_history:
        # 確保每個項目都有 "role" 和 "content" 並且非空
        if isinstance(message, dict) and "role" in message and "content" in message:
            role = message["role"]
            content = message["content"]
            # 檢查 role 是否為有效值
            if role in ["user", "assistant", "system"] and content:
                cleaned_history.append({"role": role, "content": content})
    return cleaned_history


# 清理FAQ和product list
def clean_list(data_list):
    """
    清理 FAQ 或product list，確保內容無空值或無效資料
    :param data_list: 原始的 FAQ 或product list
    :return: 乾淨的列表
    """
    return [str(item).strip() for item in data_list if isinstance(item, str) and item.strip()]

