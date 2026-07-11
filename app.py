import streamlit as st
import requests

st.title("HR Assistant 🤖")
st.write("Ask any question about the HR Policy.")

user_question = st.text_input("Enter your question")

if st.button("Ask"):
    response = requests.post(
        "http://127.0.0.1:8000/chat", json={"question": user_question}
    )

    st.write(response.json()["answer"])
