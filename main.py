import os
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Lấy API Key từ "két sắt" của hệ thống thay vì viết thẳng vào code
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

app = FastAPI()

class MessageRequest(BaseModel):
    text: str

@app.post("/chat")
async def chat_with_ai(request: MessageRequest):
    try:
        prompt = f"Bạn là một gia sư Toán lớp 9 siêu tâm lý và vui tính. Hãy giải đáp câu hỏi sau của học sinh một cách ngắn gọn, từng bước dễ hiểu: {request.text}"
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        # THÊM ĐÚNG DÒNG IN LỖI NÀY VÀO ĐÂY:
        print(f"\n[BẮT ĐƯỢC LỖI API]: {e}\n") 
        
        return {"reply": "Thầy đang bận chút việc, em hỏi lại sau nhé!"}
