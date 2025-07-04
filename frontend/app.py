import streamlit as st
import requests

# ✅ Set your backend URL here (local or Vercel)
API_BASE = "https://quiz-craft-backend.onrender.com"

st.set_page_config(page_title="QuizCraft - AI Quiz Generator", page_icon="🧠")
st.title("📘 QuizCraft: AI-Powered Question & MCQ Generator with Evaluation")

# ✅ Initialize session state
if "mcqs" not in st.session_state:
    st.session_state.mcqs = []
    st.session_state.answer_key = {}
    st.session_state.user_answers = {}
    st.session_state.score = 0

# ✅ Quiz generation form
with st.form(key="quiz_form"):
    num = st.number_input("Enter number of questions", 1, 10, 5)
    difficulty = st.selectbox("Select Difficulty Level", ["easy", "medium", "hard"])
    option = st.radio("Choose Action", ["Generate Questions", "Generate MCQs"])
    submit_button = st.form_submit_button(label="Generate")

# ✅ Handle question or MCQ generation
if submit_button:
    if option == "Generate Questions":
        try:
            res = requests.post(f"{API_BASE}/generate_questions", json={"num_questions": num, "difficulty": difficulty})
            res.raise_for_status()
            st.subheader("📝 Generated Questions")
            for i, q in enumerate(res.json()["questions"], 1):
                st.write(f"{i}. {q}")
        except Exception as e:
            st.error(f"Failed to fetch questions: {e}")

    elif option == "Generate MCQs":
        try:
            res = requests.post(f"{API_BASE}/generate_mcqs", json={"num_questions": num, "difficulty": difficulty})
            res.raise_for_status()
            st.session_state.mcqs = res.json()["mcqs"]
            st.session_state.answer_key = {item["question"]: item["answer"] for item in st.session_state.mcqs}
            st.session_state.user_answers = {}
        except Exception as e:
            st.error(f"Failed to fetch MCQs: {e}")

# ✅ Display MCQs and collect user answers
if st.session_state.mcqs:
    st.subheader("📚 Multiple Choice Questions")
    for i, item in enumerate(st.session_state.mcqs):
        st.markdown(f"**Q{i+1}: {item['question']}**")
        for opt in item["options"]:
            st.write(opt)
        st.session_state.user_answers[item['question']] = st.text_input(f"Your Answer for Q{i+1}", key=f"ans_{i}")

    if st.button("✅ Evaluate My Answers"):
        try:
            # Evaluate answers
            res = requests.post(f"{API_BASE}/evaluate", json={"user_answers": st.session_state.user_answers})
            res.raise_for_status()
            feedback = res.json().get("feedback", "No feedback returned.")

            # Score calculation
            score = 0
            for q, user_ans in st.session_state.user_answers.items():
                if user_ans.strip().upper() == st.session_state.answer_key[q].strip().upper():
                    score += 1
            st.session_state.score = score

            # Results
            st.subheader("📝 Feedback for Incorrect Answers")
            st.write(feedback)

            st.subheader("✅ Correct Answers")
            for q, correct in st.session_state.answer_key.items():
                st.markdown(
                    f"<strong>Q:</strong> {q}<br><strong>Correct Answer:</strong> {correct}",
                    unsafe_allow_html=True,
                )

            st.subheader("🎯 Your Score")
            st.success(f"You got {st.session_state.score} out of {len(st.session_state.mcqs)} correct!")

        except Exception as e:
            st.error(f"Failed to evaluate answers: {e}")
