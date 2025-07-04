from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("InDoc")

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="gemma2-9b-it",
    temperature=0.3
)

template = PromptTemplate.from_template("""
Given the document:

{text}

And the following user answers:

{answers}

Evaluate each response and provide feedback for incorrect answers. Feedback should be short and clear.
""")

def evaluate_answers(user_answers, doc_text):
    formatted = "\n".join([f"Q: {q}\nYour Answer: {a}" for q, a in user_answers.items()])
    chain = LLMChain(llm=llm, prompt=template)
    feedback = chain.invoke({"text": doc_text, "answers": formatted})
    return {"feedback": feedback['text']}
