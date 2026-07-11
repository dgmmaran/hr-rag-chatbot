from fastapi import FastAPI
from pydantic import BaseModel

from QueryProcessor import process_user_query

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Welcome to HR Chatbot API"}


@app.post("/chat")
def chat(request: ChatRequest):
    answer = process_user_query(request.question)
    return {"answer": answer}
