# Junior AI Engineer Coding Test


## 目標
1. **Prompt Engineering**
   - 設計 Quick Replies 的 Prompt 和運行函式，幫助用戶快速找到答案，提升互動性。
   - 測試 Prompt 的穩定性與生成速度。
2. **電商退貨流程設計**
   - 設計一份 Prompt，引導用戶逐步輸入退貨資訊（姓名、電話、訂單號、退貨品名、退貨理由）。
   - 確保輸入完整，並處理不完整或錯誤輸入的情況。
3. **商品描述優化 API 開發**
   - 使用 FastAPI 建立 `/summarized-description` API，將商品描述清理為精煉有重點的文字。
   - 減少 Token 消耗，優化生成速度。


## 主結構
- `quick_replies/`: 包含 Quick Replies 的 Prompt 和函式程式碼
- `api/`: 包含商品描述優化的 API 相關程式碼
- `refund_process/`: 用於退貨流程的 Prompt 設計與處理
- `test`: 所有測試程式碼

## 安裝
1. Clone 此 Repository:
   ```bash
   git clone https://github.com/MichellellehciM/junior-ai-engineer-test.git
   cd junior-ai-engineer-test
   ```
2. 建立虛擬環境:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
3. 安裝依賴：
    `pip install -r requirements.txt`

## 資料夾結構

```markdown
JUNIOR-AI-ENGINEER-TEST/
├── .venv/                         
├── quick_replies/                   # Quick Replies 模組
│   ├── quick_replies.py             
├── refine_description/               # 商品描述優化模組
│   ├── openai_utils.py               
│   ├── refine_description.py         
├── refund_process/                   # 退貨流程模組
│   ├── database.py                   
│   ├── gpt_assistant.py              
│   ├── refund_process.py             
│   ├── validation.py                 
├── tests/                            # 測試代碼
│   ├── results_for_performance.txt   
│   ├── test_quick_replies_2.py       
│   ├── test_quick_replies_performance.py
│   ├── test_quick_replies.py         
│   ├── test_refine_description.py    
│   ├── test_refund_process.py        
├── .env                             
├── .env.example                     
├── .gitignore                     
├── my_record.md                      # 開發記錄
├── README.md                         # 專案說明文件
└── requirements.txt                   # 依賴套件列表
```


-----
