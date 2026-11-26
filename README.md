# AI-Powered Document Question Answering Bot (RAG)

An AI-powered Document Question Answering Bot built using a **Retrieval-Augmented Generation (RAG)** architecture. The application allows users to upload PDF documents, indexes their contents into a ChromaDB vector database, retrieves the most relevant information using semantic search, and generates accurate answers with **Google Gemini 2.5 Flash** while providing document source citations.
---
# Features
* Upload and index PDF documents
* Automatic document chunking
* Semantic embeddings using HuggingFace
* Persistent ChromaDB vector database
* Retrieval-Augmented Generation (RAG)
* AI-powered answers using Google Gemini
* Source citations with document names and page numbers
* Command-line chatbot interface
---
# Tech Stack

| Technology             | Version          |
| ---------------------- | ---------------- |
| Python                 | 3.11+            |
| LangChain              | Latest           |
| ChromaDB               | Latest           |
| Sentence Transformers  | Latest           |
| HuggingFace Embeddings | all-MiniLM-L6-v2 |
| Google Gemini API      | Gemini 2.5 Flash |
| python-dotenv          | Latest           |
| PyPDFLoader            | Latest           |

---

# Project Structure


```
AI-DocumentQA-Bot/
│
├── data/
│   ├── machine_learning.pdf
│   ├── rag.pdf
│   ├── llm.pdf
│   └── vector_database.pdf
│
├── db/
│   └── chroma_db/
│
├── src/
│   ├── document_loader.py
│   ├── chunker.py
│   ├── vector_store.py
│   ├── ingest.py
│   ├── query.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# Architecture Overview

```
               PDF Documents
                      │
                      ▼
          Document Loader (PyPDF)
                      │
                      ▼
            Text Extraction
                      │
                      ▼
      Recursive Text Chunking
      (1000 chars, 200 overlap)
                      │
                      ▼
     HuggingFace Embeddings
(all-MiniLM-L6-v2 Sentence Transformer)
                      │
                      ▼
         ChromaDB Vector Store
                      │
              User Question
                      │
                      ▼
        Similarity Search (Top-k)
                      │
                      ▼
     Retrieved Relevant Chunks
                      │
                      ▼
      Google Gemini 2.5 Flash
                      │
                      ▼
     Final Answer + Source Citations
```

---

# Retrieval-Augmented Generation (RAG) Pipeline

### 1. Document Ingestion

* Reads all PDF files from the `data/` folder.
* Extracts text page by page.

### 2. Chunking

* Splits documents into chunks of approximately **1000 characters**.
* Uses an overlap of **200 characters** to preserve context.

### 3. Embedding Generation

* Converts each chunk into a semantic vector using:

```
sentence-transformers/all-MiniLM-L6-v2
```

### 4. Vector Storage

* Stores embeddings in a persistent **ChromaDB** database.

### 5. Retrieval

* Converts the user's question into an embedding.
* Retrieves the most relevant document chunks using similarity search.

### 6. Answer Generation

* Sends the retrieved context to **Google Gemini 2.5 Flash**.
* Generates an answer grounded only in the retrieved documents.
* Displays document names and page numbers as citations.

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-DocumentQA-Bot
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Running the Project

## Step 1: Add PDF Documents

Place all PDF files inside the `data/` folder.

Example:

```
data/
    rag.pdf
    llm.pdf
    machine_learning.pdf
```

---

## Step 2: Index the Documents

```bash
python src/ingest.py
```

This process:

* Loads PDF files
* Extracts text
* Creates chunks
* Generates embeddings
* Stores vectors inside ChromaDB

---

## Step 3: Start the Chatbot

```bash
python src/main.py
```

Example:

```
Ask a question:

> What is Retrieval-Augmented Generation?

Answer:
RAG combines information retrieval with Large Language Models...

Sources:
rag.pdf (Page 3)
llm.pdf (Page 2)
```

---

# Example Questions

* What is Retrieval-Augmented Generation?
* Explain vector databases.
* What are embeddings?
* Explain Large Language Models.
* What is semantic search?
* Explain machine learning basics.

---

# Design Decisions

## Overlapping Chunking

* Chunk Size: **1000 characters**
* Overlap: **200 characters**

This approach preserves contextual continuity between adjacent chunks and improves retrieval accuracy.

---

## Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```

Reasons:

* Lightweight
* Fast inference
* High-quality semantic embeddings
* Excellent retrieval performance

---

## Vector Database

**ChromaDB** was selected because it provides:

* Persistent local storage
* Fast similarity search
* LangChain integration
* Easy deployment
* Minimal configuration

---

## Language Model

The project uses **Google Gemini 2.5 Flash** exclusively for answer generation after relevant document retrieval.

This ensures that responses remain grounded in the uploaded documents instead of relying solely on the model's internal knowledge.

---

# Sample Workflow

```
PDF Files
     │
     ▼
Document Loader
     │
     ▼
Chunking
     │
     ▼
Embeddings
     │
     ▼
ChromaDB
     │
     ▼
User Question
     │
     ▼
Retriever
     │
     ▼
Gemini 2.5 Flash
     │
     ▼
Answer + Citations
```

---

# Future Improvements

* Streamlit web interface
* Multi-file upload
* Hybrid search (BM25 + Vector Search)
* Conversation memory
* Support for DOCX and Markdown
* OCR support for scanned PDFs
* Docker deployment
* Authentication and user management

---

# Author

**Santosh Buddhivant Tambe**

AI Engineering Internship Assignment

---

# License

This project is developed for educational and internship evaluation purposes.

