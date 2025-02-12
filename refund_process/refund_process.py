# 此檔案用來控制對話流程，並匯入其他模組

import database
import validation
import gpt_assistant

RETURN_REASONS = {
    "1": "商品損壞",
    "2": "尺寸不合",
    "3": "收到錯誤商品",
    "4": "品質問題",
    "5": "變更心意",
    "6": "其他（請輸入具體原因）"
}

def main():
    """ 讓 GPT 逐步詢問用戶，並在收集完整資訊後存入 MySQL """
    user_info = {"name": "", "phone": "", "product_name": "", "order_number": "", "reason": ""}

    while not all([user_info["name"], user_info["phone"], user_info["product_name"], user_info["order_number"]]):
        question = gpt_assistant.generate_refund_prompt(user_info)
        print(f"AI: {question}")
        user_response = input("你: ").strip()

        if "姓名" in question and not user_info["name"]:
            if validation.validate_name(user_response):
                user_info["name"] = user_response
            else:
                print("⚠️ **姓名只能包含中文、英文與 `-`，請重新輸入！**")
                continue

        elif "電話" in question and not user_info["phone"]:
            if validation.validate_phone(user_response):
                user_info["phone"] = user_response
            else:
                print("⚠️ **請輸入 8-12 位數字的電話號碼！**")
                continue

        elif "商品名稱" in question and not user_info["product_name"]:
            user_info["product_name"] = user_response  

        elif "訂單單號" in question and not user_info["order_number"]:
            if validation.validate_order_number(user_response):
                user_info["order_number"] = user_response
            else:
                print("⚠️ **訂單單號只能包含英文字母與數字，請重新輸入！**")
                continue

    while not user_info["reason"]:
        print("\n請選擇您的退貨理由（輸入數字）：")
        for num, reason in RETURN_REASONS.items():
            print(f"{num}. {reason}")

        reason_choice = input("請輸入編號選擇退貨理由: ").strip()
        if reason_choice in RETURN_REASONS:
            if reason_choice == "6":
                user_info["reason"] = input("請輸入您的退貨理由: ").strip()
            else:
                user_info["reason"] = RETURN_REASONS[reason_choice]
        else:
            print(f"⚠️ **請輸入 1-6 之間的數字對應理由！**")

    print("\n🎯 確認您的退貨資訊：")
    for key, value in user_info.items():
        print(f"{key}: {value}")

    confirmation = input("請輸入 'y' 確認提交，或 'n' 重新輸入: ").strip().lower()
    if confirmation == 'y':
        database.insert_return_request(**user_info)
        print("📢 請等候 1-2 天，會有專人聯絡您處理退貨申請。感謝您的耐心與支持！😊")

if __name__ == "__main__":
    main()
