import sqlite3
from datetime import datetime
import os

HOME_PATH = os.getenv("HOME")
WORKSPACE_PATH = os.path.join(HOME_PATH, "workspace/rag_poc")
DB_PATH = os.path.join(WORKSPACE_PATH, "database")


def init_db():
    conn = sqlite3.connect(os.path.join(DB_PATH, "chatbot.db"))
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        start_time DATETIME NOT NULL,
        end_time DATETIME,
        status TEXT,
        additional_info TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id INTEGER NOT NULL,
        sender TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        retrieved_context_id TEXT,
        metadata TEXT,
        FOREIGN KEY(conversation_id) REFERENCES conversations(id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS context_retrievals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message_id INTEGER NOT NULL,
        document_id TEXT,
        similarity_score REAL,
        snippet TEXT,
        metadata TEXT,
        FOREIGN KEY(message_id) REFERENCES messages(id)
    );
    """)

    conn.commit()
    conn.close()


def create_conversation(user_id):
    conn = sqlite3.connect(os.path.join(DB_PATH, "chatbot.db"))
    cur = conn.cursor()

    start_time = datetime.now()
    cur.execute("""
    INSERT INTO conversations (user_id, start_time, status) VALUES (?, ?, ?)
    """, (user_id, start_time, 'active'))

    conversation_id = cur.lastrowid
    conn.commit()
    conn.close()
    return conversation_id


def add_message(conversation_id, sender, content, retrieved_context_id=None, metadata=None):
    conn = sqlite3.connect(os.path.join(DB_PATH, "chatbot.db"))
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO messages (conversation_id, sender, content, retrieved_context_id, metadata)
    VALUES (?, ?, ?, ?, ?)
    """, (conversation_id, sender, content, retrieved_context_id, metadata))

    message_id = cur.lastrowid
    conn.commit()
    conn.close()
    return message_id


def add_retrieval_info(message_id, document_id, similarity_score, snippet, metadata=None):
    conn = sqlite3.connect(os.path.join(WORKSPACE_PATH, "chatbot.db"))
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO context_retrievals (message_id, document_id, similarity_score, snippet, metadata)
    VALUES (?, ?, ?, ?, ?)
    """, (message_id, document_id, similarity_score, snippet, metadata))

    conn.commit()
    conn.close()


# 사용 예시
if __name__ == "__main__":
    init_db()
    c_id = create_conversation(user_id="user123")
    user_msg_id = add_message(c_id, "user", "안녕하세요! RAG 챗봇에 대해 궁금해요.")
    # RAG 검색 결과를 저장해볼 수도 있음:
    doc_id = "doc_FAQ_001"
    snippet = "RAG는 Retrieval Augmented Generation의 약자입니다..."
    add_retrieval_info(user_msg_id, doc_id, 0.87, snippet)

    # 챗봇 답변
    bot_msg_id = add_message(c_id, "assistant", "안녕하세요! RAG 챗봇은 검색 기반 챗봇입니다.")
