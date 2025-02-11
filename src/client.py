import streamlit as st

# 페이지 제목
st.title("BA Chatbot")

# 세션 상태에 채팅 기록 저장 (앱이 새로고침되면 유지)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 채팅 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    # 사용자 메시지를 상태에 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    # print(st.session_state.messages)
    
    # API 호출
    # bot_response = call_api(user_input)  # 실제 API 호출 코드로 대체

    # 화면에 표시
    with st.chat_message("user"):
        st.markdown(user_input)

    ##### 간단한 응답 예제 (실제 AI 모델과 연동 가능) #####
    # 나중에 bot_response로 대체
    bot_response = f"🤖: {user_input}에 대해 더 알고 싶나요?"
    ########################################################

    # 챗봇 응답을 상태에 추가
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response})
    print(st.session_state.messages)

    # 챗봇 응답 표시
    with st.chat_message("assistant"):
        st.markdown(bot_response)
