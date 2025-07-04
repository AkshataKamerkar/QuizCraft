# Folder: frontend/app.py

import streamlit as st
import requests

st.title("📘 Question & MCQ Generator with Evaluation")

if "mcqs" not in st.session_state:
    st.session_state.mcqs = []
    st.session_state.answer_key = {}
    st.session_state.user_answers = {}
    st.session_state.score = 0

with st.form(key="quiz_form"):
    num = st.number_input("Enter number of questions", 1, 10, 5)
    difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])
    option = st.radio("Choose Action", ["Generate Questions", "Generate MCQs"])
    submit_button = st.form_submit_button(label="Generate")

if submit_button:
    if option == "Generate Questions":
        res = requests.post("http://localhost:8000/generate_questions", json={"num_questions": num, "difficulty": difficulty})
        st.subheader("Generated Questions")
        for i, q in enumerate(res.json()["questions"], 1):
            st.write(f"{i}. {q}")

    elif option == "Generate MCQs":
        res = requests.post("http://localhost:8000/generate_mcqs", json={"num_questions": num, "difficulty": difficulty})
        st.session_state.mcqs = res.json()["mcqs"]
        st.session_state.answer_key = {
            item["question"]: item["answer"] for item in st.session_state.mcqs
        }
        st.session_state.user_answers = {}

if st.session_state.mcqs:
    st.subheader("MCQs")
    for i, item in enumerate(st.session_state.mcqs):
        st.write(f"**Q{i+1}: {item['question']}**")
        for opt in item["options"]:
            st.write(opt)
        st.session_state.user_answers[item['question']] = st.text_input(
            f"Your Answer for Q{i+1}", key=f"ans_{i}"
        )

    if st.button("Evaluate My Answers"):
        res = requests.post("http://localhost:8000/evaluate", json={"user_answers": st.session_state.user_answers})
        feedback = res.json().get("feedback", "No feedback returned.")

        # Score tracking
        score = 0
        for q, user_ans in st.session_state.user_answers.items():
            if user_ans.strip().upper() == st.session_state.answer_key[q].strip().upper():
                score += 1

        st.session_state.score = score

        st.subheader("📝 Feedback for Incorrect Answers")
        st.write(feedback)

        st.subheader("✅ Correct Answers")
        for q, correct in st.session_state.answer_key.items():
            st.markdown(f"<strong>Q:</strong> {q}<br><strong>Correct Answer:</strong> {correct}", unsafe_allow_html=True)

        st.subheader("🎯 Your Score")
        st.success(f"You got {st.session_state.score} out of {len(st.session_state.mcqs)} correct!")
