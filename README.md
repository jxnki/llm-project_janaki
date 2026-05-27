## llm-project_janaki

## Task 1: CLI Chatbot

### Problem

Build a chatbot that runs in the terminal and can have conversations with users. The chatbot should remember previous messages and answer questions using an AI model.

### Approach

Built using Python and the Groq API with the llama-3.1-8b-instant model. The chatbot:
- Takes user input from the terminal
- Sends the conversation to the Groq API
- Gets a response back from the AI
- Remembers all previous messages

### Steps Taken

1. Set up a Python virtual environment
2. Installed libraries: groq and python-dotenv
3. Created a Groq client with an API key
4. Built the chatbot using the Chat Completions API
5. Added a list to store and remember messages
6. Added a system message to define how the chatbot behaves
7. Created a loop that keeps the chat running until user types "exit"
8. Stored the API key in a .env file

### Challenges Faced

**Challenge 1: Model Was Outdated**
- The model llama3-8b-8192 was no longer available
- Solution: Used llama-3.1-8b-instant instead, which worked fine

**Challenge 2: Keeping Messages in Memory**
- Had trouble understanding how to keep the chatbot remembering previous messages
- Solution: Stored all messages in a list and sent the entire list to the API each time

### How to Run

```bash
cd "Task 1"
python chat.py
```

Type your messages. Type `exit` to quit.

## Task 2: Web-Based PDF Chatbot

### Problem

Build a web chatbot that can answer questions from PDF files. Instead of just giving general answers, it should find the right information from the PDFs and use that to answer questions.

### Approach

Built a RAG (Retrieval Augmented Generation) system that finds relevant information in PDFs and uses it to answer questions.

How it works:
1. Load PDF files
2. Split them into smaller chunks
3. Convert chunks into vectors (embeddings)
4. Store the vectors in a database
5. When user asks a question, find similar chunks
6. Use those chunks to generate an answer

### Steps Taken

1. Set up the RAG system (rag.py)
   - Loaded PDFs
   - Split documents into 500-character chunks
   - Created embeddings from chunks
   - Stored embeddings in Chroma database
   - Built a function to retrieve chunks and get answers

2. Built the web interface (app.py)
   - Created a Streamlit app with a chat interface
   - Added memory to keep conversation history
   - Made expandable sections to show which chunks were used
   - Styled with a wide layout

3. Added logging
   - Set up rag_log.txt to track what questions were asked
   - Helps understand how the system is working

### Challenges Faced

**Challenge 1: Session State Issues**
- Chat history was disappearing when the page reloaded
- Solution: Used Streamlit's session state feature to keep messages saved

**Challenge 2: Slow Database Creation**
- Creating embeddings from PDFs took too long (15-20 seconds)
- Solution: Save embeddings to disk so they only need to be created once

**Challenge 3: Why Certain Chunks Were Retrieved**
- Didn't understand why some chunks got selected
- Solution: Realized embeddings look at meaning, not just keywords

### How to Run

```bash
cd "Task 2"
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

Type a question and press Enter. Click "Retrieved Source Chunks" to see which parts of the PDF were used.


## Project Structure

```
llm-project/
│
├── Task 1/
│   ├── chat.py
│   └── About.txt
│
├── Task 2/
│   ├── app.py
│   ├── rag.py
│   ├── Sample PDFs/
│   │   ├── notes.pdf
│   │   ├── notes2.pdf
│   │   └── notes3.pdf
│   ├── chroma_db/
│   └── About_RAG.txt
│
├── requirements.txt
├── .env
└── README.md
```

## Setup

### Prerequisites

- Python 3.10 or higher
- Groq API key (free from https://groq.com)

### 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Libraries

```bash
pip install -r requirements.txt
```

### 3. Create .env File

Create a file named `.env` in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the Project

**Task 1:**
```bash
cd "Task 1"
python chat.py
```

**Task 2:**
```bash
cd "Task 2"
streamlit run app.py
```


## What Each File Does

- `Task 1/chat.py` - CLI chatbot
- `Task 2/app.py` - Web chatbot interface
- `Task 2/rag.py` - RAG system code
- `requirements.txt` - Required libraries
- `.env` - API key (don't upload to GitHub)


## Libraries Used

- groq - AI model provider
- python-dotenv - Load environment variables
- langchain - Handle documents and embeddings
- chromadb - Store embeddings
- streamlit - Web interface
- pypdf - Read PDF files
