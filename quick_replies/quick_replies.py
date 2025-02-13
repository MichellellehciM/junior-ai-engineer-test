import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))  

def generate_quick_replies(chat_history, faq_list, product_list):
    last_user_message = None
    for message in reversed(chat_history):
        if message["role"] == "user":
            last_user_message = message["content"]
            break

    if not last_user_message:
        return ["(AI客服): 很抱歉，我沒有收到您的問題，請您再說一次哦！"]

    prompt = f"""
    你是一個友好且專業的客服助理，請根據以下對話紀錄，為 user 生成與對話紀錄相關的 Quick Replies：
    - **請根據最後一則訊息生成**
    - **請避免重複內容**
    - **只提供 5 條相關建議**
    - **不要回應過長的段落**
    
    對話記錄：
    {chat_history}

    常見問題：
    {faq_list}

    商品清單：
    {product_list}

    **使用以下格式**

    (你可能還想問): [使用者可能會問的後續問題1]
    (你可能還想問): [使用者可能會問的後續問題2]
    (你可能還想問): [使用者可能會問的後續問題3]
    (你可能還想問): [使用者可能會問的後續問題4]
    (你可能還想問): [使用者可能會問的後續問題5]

    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "你是一個友善且專業的客服助理。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.6,
        )
        
        content = response.choices[0].message.content.strip()
        replies = list(set(content.split("\n")))  # **使用 set() 來移除重複回應**
        return [reply.lstrip("- ") for reply in replies if reply.strip()]
    except Exception as e:
        print(f"生成 Quick Replies 時發生錯誤：{e}")
        return []


# 髒資料清洗
def clean_chat_history(chat_history):
    """
    清理對話紀錄，確保內容無空值或無效資料
    :param chat_history: 原始的對話紀錄
    """
    cleaned_history = []
    for message in chat_history:
        if isinstance(message, dict) and "role" in message and "content" in message:
            role = message["role"]
            content = message["content"]

            # **只保留純文字訊息**
            if isinstance(content, list):
                text_messages = [c["text"] for c in content if "text" in c]
                content = "\n".join(text_messages) if text_messages else None
            
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

