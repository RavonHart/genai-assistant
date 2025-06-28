import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.document_parser import parse_document
from models.gemini_wrapper import summarize_with_gemini
from backend.qa_engine import handle_question, generate_challenges
from backend.question_generator import evaluate_answers

# Page settings
st.set_page_config(page_title="Smart AI Research Assistant", layout="centered")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# App Title
st.markdown("<h1 style='text-align: center;'>🧠 Smart Research Assistant</h1>", unsafe_allow_html=True)
st.markdown("Upload a research paper (PDF/TXT), and let AI help you understand, summarize, and test your knowledge.")

# === Section 1: File Upload ===
st.markdown("### 📤 Upload Your Document")
uploaded_file = st.file_uploader("Choose a file to begin", type=["pdf", "txt"])

if uploaded_file:
    st.success("✅ Document uploaded successfully!")

    # === Section 2: Document Parsing ===
    with st.spinner("Reading and analyzing your document..."):
        document_text = parse_document(uploaded_file)

    # === Section 3: Auto Summary ===
    st.markdown("### 📝 Auto Summary")
    with st.spinner("Generating concise summary..."):
        summary = summarize_with_gemini(document_text)
    st.markdown(summary)

    # === Section 4: Mode Selection ===
    st.markdown("### 🎯 Choose Interaction Mode")
    mode = st.radio("Select a mode", ("Ask Anything", "Challenge Me"), horizontal=True)

    # === Section 5a: Ask Anything Mode ===
    if mode == "Ask Anything":
        st.markdown("### 🤔 Ask Anything About the Document")
        question = st.text_input("Type your question below:")

        if question:
            with st.spinner("Thinking..."):
                answer, snippet = handle_question(document_text, question, st.session_state.chat_history)
            st.success("✅ Answer generated!")

            st.markdown(f"**💬 Answer:** {answer}")
            st.markdown("📌 **Supporting Snippet:**")
            st.code(snippet, language="text")

            # Save Q&A to chat history
            st.session_state.chat_history.append({"question": question, "answer": answer})

    # === Section 5b: Challenge Me Mode ===
    elif mode == "Challenge Me":
        st.markdown("### 🧩 Logic-Based Challenge Questions")
        with st.spinner("Generating questions..."):
            questions = generate_challenges(document_text)

        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1}:** {q}")
            user_input = st.text_input(f"Your answer to Q{idx+1}:")

            if user_input:
                with st.spinner("Evaluating your answer..."):
                    feedback = evaluate_answers(document_text, q, user_input)
                st.markdown(f"**🧠 Feedback:** {feedback}")

    # === Section 6: Chat/Q&A History ===
    if st.session_state.chat_history:
        with st.expander("🧠 View Previous Questions & Answers"):
            for i, qa in enumerate(reversed(st.session_state.chat_history[-5:]), 1):
                st.markdown(f"**Q{i}:** {qa['question']}")
                st.markdown(f"**A{i}:** {qa['answer']}")

    # === Optional: Clear Memory Button ===
    st.markdown("---")
    if st.button("🔄 Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared. Ask fresh questions!")

else:
    st.info("👆 Please upload a PDF or TXT file to get started.")