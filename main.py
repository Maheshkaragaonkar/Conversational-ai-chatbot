import streamlit as st
from chatbot_logic import get_response

st.title("🧠 Conversational AI Chatbot ")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

for sender, msg in st.session_state.chat_history[::-1]:
    st.markdown(f"**{sender}:** {msg}")
