 # 開發過程記錄

## 2025-02-05 環境設置
- 建立新的repository名稱junior-ai-engineer-test
    - 初始化README.md和.gitignore
    - git clone到本地 git clone https://github.com/MichellellehciM/junior-ai-engineer-test.git
    cd junior-ai-engineer-test
- 建立開發環境
    - 建立資料夾(quick_replies, api, refund_process)
    - 虛擬環境 python -m venv .venv
    - 啟用虛擬環境 .venv/Scripts/activate 
    - 新增README.md
    - 新增requirements.txt

## 2025-02-06 完成quick replies
- 安裝 openai 和 python-dotenv 套件  `pip install openai`  `pip install python-dotenv` 並將其添加到requirement.txt `pip freeze > requirements.txt`
- 閱讀OpenAI相關文件 (https://github.com/openai/openai-python/blob/main/README.md)
    - 新增OpenAI secret key (https://platform.openai.com/api-keys)
    - 建立.env
    - 建立quick_replies、clean_chat_history、clean_list等functions
    - Python API測試 `python -m unittest tests/test_quick_replies.py`
    - () 待完成 設計test 50次
## 2025-02-07 完成資料庫設置
- 安裝和設定mysql(之前專案是用Postgres,想練習用看看其他的sql) 儲存客戶資訊
    - 建立新database: RefundProcess
    - 建立table: refunds
    - 建立columns: name, phone, order_number, product_name, reason, created_at
- 安裝 Python 的 MySQL 連接器庫 `pip install mysql-connector-python`
- 安裝 MySQL extension 到 VSCode + 完成 connect to server 設定
## 2025-02-10 完成return process
- 新增 refund_process.py （定義 prompt 和運行函式）
- AI機器人return process測試: 
    - 輸入指令`python refund_process/refund_process.py` 依序輸入退貨資料
- 新增 test_refund_process.py （測試函式是否運作正常）
    - 輸入指令`python -m unittest tests/test_refund_process.py`
