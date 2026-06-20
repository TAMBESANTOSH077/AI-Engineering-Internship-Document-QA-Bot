import streamlit as st
from src.query import ask_question

st.set_page_config(
    page_title="AI Document Q&A Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Document Q&A Assistant")

question = st.text_input("Ask a question about your documents")

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching documents and generating answer..."):

            answer, docs = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for doc in docs:

            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "-")

            st.write(f"📄 **{source}** (Page {page})")