import streamlit as st
from faq_data import faq

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Learning Assistant")

# Sidebar
st.sidebar.title("📚 Categories")

st.sidebar.info("""
AI
Python
SQL
Data Analytics
Machine Learning
""")

# Clear Chat Button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input
question = st.text_input("Ask a question")

if question:
    answer = faq.get(
        question.lower(),
        "Sorry, I don't know the answer yet."
    )

    st.session_state.messages.append(
        {"question": question, "answer": answer}
    )

# Display Chat History
for chat in st.session_state.messages:
    st.write(f"🧑 You: {chat['question']}")
    st.write(f"🤖 Bot: {chat['answer']}")

# Footer
st.markdown("---")
st.caption("Built by Abdiisse-Tech 🚀")