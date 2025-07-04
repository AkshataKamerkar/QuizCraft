from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import json

load_dotenv()
GROQ_API_KEY = os.getenv("InDoc")

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="gemma2-9b-it",
    temperature=0.3
)

template = PromptTemplate.from_template("""
You are an expert education assistant.
Based on the following content:

{text}

Generate {k} high-quality multiple choice questions of {difficulty} difficulty.
Each question must be structured as a JSON object with the following keys:
- "question": the question text
- "options": a list of 4 options ["A. ...", "B. ...", "C. ...", "D. ..."]
- "answer": the correct option letter ("A", "B", "C", or "D")
Return a list of exactly {k} such objects as a JSON array.
""")

def generate_mcqs(text, k, difficulty):
    chain = LLMChain(llm=llm, prompt=template)
    response = chain.invoke({"text": text, "k": k, "difficulty": difficulty})
    try:
        return json.loads(response["text"])
    except json.JSONDecodeError:
        return []
