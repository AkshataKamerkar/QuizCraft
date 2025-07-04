from fastapi import FastAPI
from pydantic import BaseModel
from utils.parser import parse_document
from utils.question_gen import generate_questions
from utils.mcq_gen import generate_mcqs
from utils.evaluator import evaluate_answers

app = FastAPI()

DOCUMENT_TEXT = parse_document("document.pdf")

class QuestionRequest(BaseModel):
    num_questions: int
    difficulty: str

class MCQRequest(BaseModel):
    num_questions: int
    difficulty: str

class EvaluationRequest(BaseModel):
    user_answers: dict

@app.get("/")
def home():
    return {"message": "QuizCraft backend is running."}

@app.post("/generate_questions")
def get_questions(req: QuestionRequest):
    return {"questions": generate_questions(DOCUMENT_TEXT, req.num_questions, req.difficulty)}

@app.post("/generate_mcqs")
def get_mcqs(req: MCQRequest):
    return {"mcqs": generate_mcqs(DOCUMENT_TEXT, req.num_questions, req.difficulty)}

@app.post("/evaluate")
def evaluate(req: EvaluationRequest):
    return evaluate_answers(req.user_answers, DOCUMENT_TEXT)
