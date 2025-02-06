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
    - 待完成 test 50次
