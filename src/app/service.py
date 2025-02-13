# services/chatbot_service.py
from repository import *

class ChatbotService:
    def __init__(self):
        # 데이터 저장소 인스턴스 생성 (실제 환경에서는 의존성 주입 등을 고려)
        self.repo = ChatbotRepository()
    
    def get_response(self, message: str) -> str:
        """
        간단한 로직을 통해 메시지에 대한 응답을 생성합니다.
        실제 서비스에서는 NLP 처리, 외부 API 연동 등 복잡한 로직을 구현할 수 있습니다.
        """
        # 사용자의 메시지 저장
        self.repo.save_message(message)
        
        # 예시: 메시지에 "안녕"이 포함되어 있으면 인사말 응답
        if "안녕" in message:
            response = "안녕하세요! 무엇을 도와드릴까요?"
        else:
            response = "죄송해요, 무슨 말인지 잘 이해하지 못했어요."
        
        # 챗봇 응답 저장
        self.repo.save_response(response)
        
        return response

