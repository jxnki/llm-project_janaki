import streamlit as st
from rag import ask_rag

st.set_page_config(layout="wide")

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly assistant that explains things clearly."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"]) 

question = st.chat_input("Ask a question")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    answer, retrieved_docs = ask_rag(question, st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        st.write(answer)

    with st.expander("Retrieved Source Chunks"):
        for i, doc in enumerate(retrieved_docs, 1):
            st.write(f"Chunk {i}")
            st.write(doc.page_content)