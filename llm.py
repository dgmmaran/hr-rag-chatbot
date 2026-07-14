from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def query_llm_with_context(query: str, context: str):
    system_content = """You are an HR Policy Assistant.

Answer the user's question only using the provided HR policy context.
Do not make assumptions or add information that is not present in the context.

Response Guidelines:
- Match the length of your answer to the user's question.
- For simple factual questions (for example, work timings, leave balance, office location, probation period), provide a short and direct answer in 1-3 sentences.
- For questions asking for explanations, procedures, eligibility, or comparisons, provide a structured answer using bullet points when appropriate.
- If the answer contains multiple steps or conditions, use bullet points for clarity.
- If the context does not contain enough information, reply exactly:
  "I couldn't find this information in the HR policy."
- Do not mention the context, documents, or retrieved text in your answer.
- Be clear, professional, and concise.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"Query: {query}\n\nContext:\n{context}"},
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content
