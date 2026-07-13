import streamlit as st
import requests

st.title("HR Assistant 🤖")
st.write("Ask any question about the HR Policy.")

user_question = st.text_input("Enter your question")

if st.button("Ask"):
    API_URL = "https://hr-rag-chatbot-wz87.onrender.com/chat"

    response = requests.post(API_URL, json={"question": user_question})

    st.write(response.json()["answer"])
