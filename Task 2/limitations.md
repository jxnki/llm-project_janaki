# Current Limitations and Possible Improvements

## 1. Only PDF Files Supported

**Current Limitation:**
Currently, the system works only with PDF documents.

**Possible Solution:**
Add support for DOCX, TXT, and other file formats using additional document loaders.


## 2. No File Upload Option

**Current Limitation:**
Users must manually place files inside the project folder.

**Possible Solution:**
Add a file upload feature in the Streamlit interface.


## 3. Fixed Chunk Size

**Current Limitation:**
Some answers may lose important context because the chunk size is fixed.

**Possible Solution:**
Try larger chunk sizes and chunk overlap values.


## 4. Similar Chunks Retrieved

**Current Limitation:**
For some queries, the retrieved chunks contain very similar information.

**Possible Solution:**
Use hybrid search to improve chunk diversity.


## 5. No Long-Term Chat Memory

**Current Limitation:**
Conversation history is lost when the application is restarted.

**Possible Solution:**
Save chat history locally and reload it when the application starts.


## 6. Source PDF Not Displayed

**Current Limitation:**
The system does not show which PDF a retrieved chunk came from.

**Possible Solution:**
Store filename metadata with the chunks and display it in the user interface.


## 7. Retrieval Accuracy Can Be Improved

**Current Limitation:**
The system currently uses only semantic similarity search.

**Possible Solution:**
Combine semantic search with keyword-based search to improve retrieval accuracy.
