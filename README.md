# 🤖 HR RAG Chatbot

An AI-powered HR Assistant that answers employee questions based on the company's HR Policy document using Retrieval Augmented Generation (RAG).

---

## 📌 Project Overview

This chatbot enables employees to ask HR-related questions in natural language and receive accurate answers from the HR Policy PDF instead of searching through lengthy documents.

Example Questions:

- What are the working hours?
- How many casual leaves are allowed?
- What is the maternity leave policy?
- What is the notice period?

---

## 🚀 Features

- AI-powered HR Assistant
- RAG (Retrieval Augmented Generation)
- Semantic Search using Pinecone
- OpenAI GPT for answer generation
- FastAPI Backend
- Streamlit Frontend
- PDF Document Processing
- Embedding Generation
- Context-based Responses

---

## 🏗️ System Architecture

```
Employee
      │
      ▼
Streamlit UI
      │
      ▼
FastAPI Backend
      │
      ├────────► Pinecone Vector Database
      │
      └────────► OpenAI GPT Model
                      │
                      ▼
              AI Generated Response
```

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- OpenAI API
- Pinecone
- LangChain
- PyPDF
- dotenv

---

## 📂 Project Structure

```
.
├── api.py
├── app.py
├── QueryProcessor.py
├── vectorstore.py
├── embedder.py
├── chunker.py
├── pdfreader.py
├── dataprocessor.py
├── llm.py
├── requirements.txt
├── resources/
│   └── HRPolicy.pdf
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dgmmaran/hr-rag-chatbot.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add:

```text
OPENAI_API_KEY=your_api_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX=your_index_name
```

Run FastAPI

```bash
uvicorn api:app --reload
```

Run Streamlit

```bash
streamlit run app.py
```

---

## 💬 Sample Questions

- What is the work timing policy?
- What is the annual leave policy?
- Can I work from home?
- What is the probation period?
- How many sick leaves are allowed?

---

## 🔒 Security

- API Keys stored in `.env`
- `.env` excluded using `.gitignore`
- No sensitive credentials committed to GitHub

---

## 📈 Future Enhancements

- User Authentication
- Conversation History
- Chat Memory
- Admin Dashboard
- Source Citation
- Multi-PDF Support
- Feedback System
- Logging & Monitoring
- Docker Deployment
- Kubernetes Deployment

---

## 👨‍💻 Author

**Maran**

AI Engineer | AI Solution Architect 
