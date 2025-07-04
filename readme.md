
# 📘 Question & MCQ Generator with Evaluation

An interactive application built with **FastAPI**, **LangChain**, **ChatGroq**, and **Streamlit** that allows users to:
- 📄 Generate questions or MCQs from a backend PDF document.
- 🎯 Select difficulty level: Easy, Medium, Hard.
- 📝 Submit answers and receive feedback.
- ✅ Get automatic evaluation and scoring.

---

## 🚀 Features

- ✅ **PDF-based document ingestion**
- 🎓 **Question & MCQ generation** powered by **LLMs (Groq + LangChain)**
- 🔄 **Session-based interaction** with **Streamlit**
- 📊 **Answer evaluation** with LLM-generated feedback
- ⭐ **Scoring system** to track performance
- ⚙️ **Difficulty selection** (easy, medium, hard)

---

## 🧱 Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Frontend     | Streamlit              |
| Backend      | FastAPI                |
| LLMs         | ChatGroq (Mixtral / Gemma) |
| Document Parsing | LlamaParse         |
| Prompt Engine | LangChain             |
| Embeddings (Optional) | SentenceTransformers |

---

## 📂 Project Structure

```
question-mcq-app/
│
├── backend/
│   ├── app.py                  # FastAPI backend app
│   └── utils/
│       ├── parser.py           # PDF to text using LlamaParse
│       ├── question_gen.py     # Question generation using LLM
│       ├── mcq_gen.py          # MCQ generation as structured JSON
│       └── evaluator.py        # Evaluate user answers via LLM
│
├── frontend/
│   └── app.py                  # Streamlit UI for interaction
│
├── document.pdf                # Source content document
├── .env                        # API keys for ChatGroq
├── requirements.txt            # Dependency file
└── README.md                   # You’re here
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/question-mcq-app.git
cd question-mcq-app
```

### 2. Create a virtual environment
```bash
python -m venv env
source env/bin/activate   # or env\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key in `.env`
```
InDoc=your_groq_api_key
```

### 5. Add your `document.pdf` in the root directory

---

## ⚙️ Running the App

### Start the Backend (FastAPI)
```bash
cd backend
uvicorn app:app --reload
```

### Start the Frontend (Streamlit)
```bash
cd ../frontend
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧪 Example Use Case

> 📘 Select: "Generate MCQs"  
> 🧠 Choose: Difficulty = *Medium*  
> ✍️ Answer questions  
> 🔍 Click “Evaluate My Answers”  
> 🎯 View your score & correct answers with helpful feedback

---

## ✅ Sample API Endpoints

- `POST /generate_questions`:  
  Body → `{ "num_questions": 5, "difficulty": "medium" }`

- `POST /generate_mcqs`:  
  Body → `{ "num_questions": 5, "difficulty": "hard" }`

- `POST /evaluate`:  
  Body → `{ "user_answers": { "Q1": "B", "Q2": "A", ... } }`

---

## 🧠 Powered By

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq API](https://console.groq.com/)
- [LlamaParse](https://github.com/run-llama/llama-parse)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

## 📌 Future Improvements

- ✅ User authentication
- 📊 Admin dashboard with leaderboard
- 🧠 Explanation for each correct/incorrect answer
- 🔄 Allow user-uploaded PDFs
- 🧾 Export results as PDF or CSV

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
