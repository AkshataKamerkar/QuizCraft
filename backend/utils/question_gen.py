from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
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
You are a critical thinking question generator trained to extract deep insights from complex texts. Analyze the following content thoroughly and generate exactly {k} {difficulty}-level thought-provoking questions that are grounded solely in the information and context present within the text.

Do not introduce any external knowledge.
Ensure the questions challenge understanding, inference, interpretation, or application.
Avoid listing or numbering the questions.
Your response should consist of only the questions, with no preamble, no explanations, and no formatting beyond plain text.
    
Input:  {text}
Output: Only the questions, plain text, no numbering, no explanation
                                        """)

def generate_questions(text, k, difficulty):
    chain = LLMChain(llm=llm, prompt=template)
    result = chain.invoke({"text": text, "k": k, "difficulty": difficulty})
    return [q.strip() for q in result['text'].split("\n") if q.strip()]
