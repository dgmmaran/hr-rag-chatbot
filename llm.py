from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def query_llm_with_context(query: str, context: str):
    system_content = """You are an HR Policy Assistant.

Use only the provided HR policy to answer HR questions.
Do not guess or add missing information.
Reply naturally to greetings.
Keep answers concise.
Use bullets only if needed.
If the answer is not found, reply:
"I couldn't find this information in the HR policy."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"Query: {query}\n\nContext:\n{context}"},
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content
