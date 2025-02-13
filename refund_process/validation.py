# 此檔案負責使用者輸入驗證邏輯

import re


def validate_name(name):
    """ 姓名只能包含中文、英文與 `-` """
    return bool(re.match(r"^[\u4e00-\u9fa5a-zA-Z\s-]+$", name))

def validate_phone(phone):
    """ 電話號碼必須是 8-12 位數字 """
    return phone.isdigit() and 8 <= len(phone) <= 12

def validate_order_number(order_number):
    """ 訂單單號只能包含英文字母與數字 """
    return bool(re.match(r"^[A-Za-z0-9]+$", order_number))
