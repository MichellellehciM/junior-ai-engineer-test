# 此模組用來處理 OpenAI 相關功能（封裝 API + retry 機制）
import openai
import time

def call_openai_with_retry(prompt, retries=3):
    """呼叫 OpenAI API，並在失敗時自動重試"""
    for i in range(retries):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=320,
                temperature=0.0    
            )
            return response.choices[0].message.content.strip()
        except openai.error.OpenAIError as e:
            if i < retries - 1:
                time.sleep(2)  
                continue
            else:
                raise e  
