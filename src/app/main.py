from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from service import *

app = FastAPI(title="FastAPI Chatbot Service")

class ChatRequest(BaseModel):
    '''
    입력 형식을 지정
    '''
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/ask", response_model=ChatResponse)
async def ask_chatbot(query: ChatRequest):
    '''
    사용자가 보낸 메시지를 기반으로 챗봇 응답을 생성하는 엔드포인트
    '''
    service = ChatbotService() # 서비스 객체 생성
    
    # 챗봇 응답 생성
    answer = service.get_response(query.message)
    
    return ChatResponse(response=answer)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)