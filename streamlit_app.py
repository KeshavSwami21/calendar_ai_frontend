import streamlit as st
import requests

st.title("🗓️ Google Calendar Booking Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask me to book your appointment...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Processing..."):
        res = requests.post("https://calendar-ai-backend-nmvc.onrender.com/chat", json={"message": user_input})
        # st.write("Status Code:", res.status_code)
        # st.write("Raw Response:", res.text)
        try:
            bot_response = res.json()["response"]
        except Exception as e:
            bot_response = f"Error decoding backend response: {e}"
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])