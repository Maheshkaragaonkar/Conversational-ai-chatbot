import streamlit as st
from chatbot_logic import get_response

st.set_page_config(page_title="Local ChatBot", page_icon="🤖")
st.title("🤖 Local ChatBot (Mistral via Ollama)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if st.button("Send") and user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.session_state.user_input = ""

for sender, message in st.session_state.chat_history[::-1]:
    st.markdown(f"**{sender}:** {message}")

