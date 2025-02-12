# Refund Process 開發指南

## `refund_process.py` (核心功能開發)
此專案負責處理 退貨申請，透過 Python + MySQL 建立一個互動式的 退貨系統，讓使用者輸入訂單資訊後，將數據存入 資料庫

### ✅ 開發步驟：
1. **建立MySQL資料庫連結**
   - 確保 API Key 來自環境變數。

2. **定義 `generate_quick_replies()`**
   - 解析 `chat_history`，找到使用者最後的訊息。
   - 根據 `faq_list` 和 `product_list` 設計 prompt，確保 AI 生成的回覆有關聯性。
   - 使用 OpenAI GPT-4 API 來生成回覆，確保輸出結構清晰。
   - 提供一個 fallback 訊息，當無法產生合適回覆時，回傳預設的回應。

3. **清理髒數據**
   - `clean_chat_history()` 清理對話記錄，移除不必要的雜訊。
   - `clean_list()` 清理 FAQ 和產品清單，確保輸入格式正確。

4. **prompt 設計**
   - 透過 prompt 設計，找出影響回應時間的因素，例如：
     - 減少不必要的歷史對話內容。
     - 縮短 prompt 長度，提高 API 回應速度。

---

### ✅ 測試：
## 1. `test_quick_replies.py` (單元測試1: 根據對話紀錄生成5個客戶可以問的問題)

## 2. `test_quick_replies_2.py` (單元測試2: 根據對話紀錄生成5個客戶可以問的問題)

## 3. `test_quick_replies_performance.py` (效能測試: 生成50次quick replies, 並且記錄時間)



---

## 如何優化 Quick Replies
### 🚀 **減少 Token 消耗**
- 限制歷史對話長度，保留最相關的訊息。 (之後可開發)
- 使用簡潔的 prompt，避免多餘的上下文。

### ⚡ **提高回應速度**
- 減少 `temperature` 以確保回應穩定，不讓 AI 產生過多變異性。
- 使用 `max_tokens` 限制回應長度，加快處理速度。

---

## 📌 **開發結論**
這個專案的核心目標是透過 OpenAI API 來自動生成 Quick Replies，並透過測試來確保：
1. **輸出穩定**（格式固定，數量正確）。
2. **效能優化**（減少 Token 消耗，提高回應速度）。
3. **錯誤處理**（處理髒數據與不完整輸入）。

這樣能確保 Quick Replies 系統可以有效運行，並在 AI 對話中提升使用者體驗。 🚀
