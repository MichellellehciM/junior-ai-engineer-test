# 此檔案用來定義 GPT-4o 的對話模板，以及生成退貨流程的對話內容。

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
你是一個禮貌的電商客服 AI，幫助用戶完成退貨申請。
**請只詢問還沒有填寫的欄位，不要重複詢問已填寫的內容，一次問一題！**
如果用戶輸入格式錯誤，請友善地提示修改。

### **目前已收集到的資訊**
- **姓名:** {name}
- **電話:** {phone}
- **商品名稱:** {product_name}
- **訂單單號:** {order_number}

請根據 **尚未填寫的欄位**，**只問還沒填寫的問題**，避免多餘的對話或客套話。
"""

def generate_refund_prompt(user_info):
    """ 根據當前已填寫的資訊，讓 GPT 只問還沒填的欄位 """
    prompt = PROMPT_TEMPLATE.format(
        name=user_info["name"] or "未填寫",
        phone=user_info["phone"] or "未填寫",
        product_name=user_info["product_name"] or "未填寫",
        order_number=user_info["order_number"] or "未填寫",
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "你是一個智能客服，請幫助用戶完成退貨申請。"},
                  {"role": "user", "content": prompt}],
        max_tokens=50,
        temperature=0.3  
    )

    return response.choices[0].message.content.strip()
