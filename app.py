"""import streamlit as st
import requests

st.title("HR Assistant 🤖")
st.write("Ask any question about the HR Policy.")

user_question = st.text_input("Enter your question")

if st.button("Ask"):
    API_URL = "https://hr-rag-chatbot-wz87.onrender.com/chat"

    response = requests.post(API_URL, json={"question": user_question})

    st.write(response.json()["answer"])"""

import streamlit as st
import requests

# -------------------------------
# Page Title
# -------------------------------
st.title("HR Assistant 🤖")
st.write("Ask any question about the HR Policy.")

API_URL = "https://hr-rag-chatbot-wz87.onrender.com/chat"

# -------------------------------
# Initialize Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Display Previous Messages
# -------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# Chat Input
# -------------------------------
prompt = st.chat_input("Ask your HR question...")

if prompt:
    # Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Store User Message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call FastAPI
    with st.spinner("Searching HR Policy..."):
        response = requests.post(API_URL, json={"question": prompt})

        answer = response.json()["answer"]

    # Display Assistant Message
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Store Assistant Message
    st.session_state.messages.append({"role": "assistant", "content": answer})
