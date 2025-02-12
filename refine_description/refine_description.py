
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from .openai_utils import call_openai_with_retry

load_dotenv()

app = FastAPI()

class ProductDescriptionRequest(BaseModel):
    description: str  

class ProductDescriptionResponse(BaseModel):
    summarized_description: str
    status: str
    error: str | None = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# API Endpoint: /summarized-description
@app.post("/summarized-description", response_model=ProductDescriptionResponse)
async def summarize_description(request: ProductDescriptionRequest):
    """
    接收商品描述，並生成更簡潔、結構化的描述
    """
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="Missing OpenAI API Key")

    try:
        prompt = (
            "請根據以下商品描述，生成精煉、有重點且結構化的摘要，避免冗長，確保摘要完整"
            "請遵守以下要求：\n"
            "-刪除無關資訊，避免過度修飾與行銷用語\n"
            "-適當分配 token，確保句子完整、流暢且易讀，避免內容截斷。\n\n"
            "-條列出特點和注意事項 `1, 2, 3 ...`(特點和注意數項最多各8行，每行最多15字)\n"
            f"商品描述：{request.description}\n\n"
            "請輸出:\n"

            " 品名:<簡潔名稱>\n"
            "✨特點\n"
            " 1.<精簡特點 1>\n"
            " 2.<精簡特點 2>\n"
            " 3.<精簡特點 3>\n"

            "🔺注意事項\n"
            " 1.<注意事項 1>\n"
            " 2.<注意事項 2>\n"
            " 3.<注意事項 3>\n"
        )

        # 呼叫封裝好的 OpenAI API 函數
        openai_summary = call_openai_with_retry(prompt)

        return ProductDescriptionResponse(
            summarized_description=openai_summary,
            status="success",
            error=None
        )

    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API 錯誤：{str(e)}")

    except Exception as e:
        return ProductDescriptionResponse(
            summarized_description="",
            status="error",
            error=str(e)
        )
