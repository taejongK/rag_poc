# repositories/chatbot_repository.py
class ChatbotRepository:
    def __init__(self):
        # 임시 메모리 내 데이터 저장 (실제 서비스에서는 데이터베이스 등을 사용)
        self.chat_history = []
    
    def save_message(self, message: str):
        """
        사용자의 메시지를 저장하는 메서드.
        """
        self.chat_history.append({"type": "user", "content": message})
    
    def save_response(self, response: str):
        """
        챗봇의 응답을 저장하는 메서드.
        """
        self.chat_history.append({"type": "bot", "content": response})
    
    def get_history(self):
        """
        저장된 채팅 내역을 반환하는 메서드.
        """
        return self.chat_history
