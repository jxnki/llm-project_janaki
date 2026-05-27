from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from groq import Groq
from dotenv import load_dotenv
import os
import logging

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
logging.basicConfig(filename="rag_log.txt",level=logging.INFO)

pdf_files=["Sample PDFs/notes.pdf","Sample PDFs/notes2.pdf","Sample PDFs/notes3.pdf"]

documents=[]
for file in pdf_files:
    loader=PyPDFLoader(file)
    documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

if os.path.exists("chroma_db"):
    vectorstore = Chroma(embedding_function=embeddings, persist_directory="chroma_db")
else:
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="chroma_db")
messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

def ask_rag(question, messages):
    logging.info(f"User Question: {question}")
    retrieved_docs = vectorstore.similarity_search(question, k=3)
    logging.info(f"Retrieved {len(retrieved_docs)} chunks")
    
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    prompt = f"""
Use ONLY the context below to answer the question.

Give a clear answer in 4-6 sentences.
If the context contains bullet points, turn them into a short explanation.

If the answer is not found in the context, say:
"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}
"""

    temp_messages = messages.copy()
    temp_messages.append({"role": "user", "content": prompt})

    chat_completion = client.chat.completions.create(
        messages=temp_messages,
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_tokens=500,
    )

    answer = chat_completion.choices[0].message.content
    logging.info(f"AI Answer: {answer}")
    
    return answer, retrieved_docs