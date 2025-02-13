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
- 安裝 openai 和 python-dotenv 套件 並將其添加到requirement.txt 
- 閱讀OpenAI相關文件 (https://github.com/openai/openai-python/blob/main/README.md)
    - 新增OpenAI secret key (https://platform.openai.com/api-keys)
    - 建立.env
    - 建立quick_replies, clean_chat_history, clean_list等functions
    - (測試 1) 髒資料處理對話紀錄 + 生成五個 Quick Replies
        - 輸入指令`python -m unittest tests/test_quick_replies.py`
    - (測試 2) 根據對話紀錄 生成五個 Quick Replies
        - 輸入指令`python -m unittest tests/test_quick_replies_2.py`
    - (測試 3) 生成 50 次 Quick Replies + 紀錄 test 平均時間
        - 輸入指令`python -m unittest tests/test_quick_replies_perfomance.py` 2025-02-12完成

## 2025-02-07 完成資料庫設置
- 安裝和設定mysql(之前專案是用Postgres,想練習用看看其他的sql) 儲存客戶資訊
    - 建立新database: RefundProcess
    - 建立table: refunds
    - 建立columns: name, phone, order_number, product_name, reason, created_at
- 安裝 Python 的 MySQL 連接器庫 mysql-connector-python
- 安裝 MySQL extension 到 VSCode + 完成 connect to server 設定

## 2025-02-10 完成return process
- 建立 refund_process.py （控制對話流程，並匯入其他模組，包含 database.py、 gpt_assistant.py、validation.py）
- (測試 4) AI引導詢問客戶退款資訊 + 儲存於資料庫
    - 輸入指令`python refund_process/refund_process.py` 
- (測試 5) 當退款資訊缺少，AI 引導詢問缺少欄位
    - 輸入指令`python -m unittest tests/test_refund_process.py`

## 2025-02-11 ~ 2025-02-12 完成API development  , refine description
- 建立 refine_description.py 
    - 建立 FastAPI APP 
    - 定義請求/回應模型
    - 定義路由 /summarized-description
- 新增捕捉錯誤程式碼
    - 1️⃣ 捕捉 OpenAI API 相關錯誤（openai.error.OpenAIError）
    - 2️⃣ 捕捉所有其他未知錯誤（Exception）
- 安裝 fastapi 以及 uvicorn 
    - 啟動 FastAPI 應用，並讓 uvicorn 伺服器運行 API 服務: `python -m uvicorn refine_description:app --reload`
- (測試 6) Postman API請求測試  URL http://localhost:8000/summarized-description
    - POST → 在body貼上要測試的內容(JSON)
- (測試 7) FastAPI向OpenAI取得精簡化的商品描述
    - 輸入指令`python -m unittest tests/test_refine_description.py`
