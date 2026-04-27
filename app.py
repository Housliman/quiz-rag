import streamlit as st
import os
from rag import process_pdf, retrieve_context
from quiz import generate_quiz

st.set_page_config(page_title="PDF Quiz Generator", layout="centered")


def main():
    st.title("PDF Quiz Generator")
    st.markdown("Upload a PDF and test your knowledge!")

    if "quiz" not in st.session_state:
        st.session_state.quiz = None
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    with st.sidebar:
        st.header("Settings")
        uploaded_file = st.file_uploader("Upload PDF", type="pdf")
        num_questions = st.slider("Number of Questions", 5, 15, 5)

        if uploaded_file and st.button("Generate Quiz"):
            with st.spinner("Processing PDF and generating quiz..."):
                try:
                    vector_store = process_pdf(uploaded_file)
                    if vector_store:
                        context = retrieve_context(vector_store)
                        quiz_data = generate_quiz(context, num_questions)
                        st.session_state.quiz = quiz_data.get("questions", [])
                        st.session_state.current_question = 0
                        st.session_state.answers = {}
                        st.session_state.quiz_submitted = False
                        st.success("Quiz generated!")
                    else:
                        st.error("Could not extract text from PDF.")
                except Exception as e:
                    st.error(f"Error: {e}")

    if st.session_state.quiz and not st.session_state.quiz_submitted:
        questions = st.session_state.quiz
        current_idx = st.session_state.current_question
        q = questions[current_idx]
        st.subheader(f"Question {current_idx + 1} of {len(questions)}")
        st.write(q["question"])
        choices = q["choices"]
        choice_labels = [f"{k}: {v}" for k, v in choices.items()]
        selected = st.radio(
            "Select your answer:", choice_labels, key=f"q_{current_idx}"
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            if current_idx > 0:
                if st.button("Previous"):
                    st.session_state.answers[current_idx] = selected[0]
                    st.session_state.current_question -= 1
                    st.rerun()

        with col2:
            if current_idx < len(questions) - 1:
                if st.button("Next"):
                    st.session_state.answers[current_idx] = selected[0]
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Submit Quiz"):
                    st.session_state.answers[current_idx] = selected[0]
                    st.session_state.quiz_submitted = True
                    st.rerun()

    elif st.session_state.quiz_submitted:
        st.header("Quiz Results")

        correct_count = 0
        questions = st.session_state.quiz

        for i, q in enumerate(questions):
            user_ans = st.session_state.answers.get(i)
            is_correct = user_ans == q["answer"]
            if is_correct:
                correct_count += 1

            with st.expander(f"Question {i + 1}: {'✅' if is_correct else '❌'}"):
                st.write(f"**Question:** {q['question']}")
                st.write(f"**Your Answer:** {user_ans}")
                st.write(f"**Correct Answer:** {q['answer']}")
                st.write(f"**Explanation:** {q['explanation']}")

        score_pct = (correct_count / len(questions)) * 100
        st.metric(
            "Final Score", f"{correct_count} / {len(questions)}", f"{score_pct:.1f}%"
        )

        if st.button("Start New Quiz"):
            st.session_state.quiz = None
            st.session_state.quiz_submitted = False
            st.rerun()


if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        st.warning("Please set your GROQ_API_KEY in the .env file.")
    main()
