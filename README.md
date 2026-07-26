<div align="center">

# ⚖️ Vincenzo: AI Lawyer Assistant

### *AI-Powered Legal Research & Analysis using Retrieval-Augmented Generation (RAG)*

<p align="center">
An intelligent legal assistant that combines <strong>Large Language Models</strong>, <strong>Semantic Search</strong>, and <strong>Retrieval-Augmented Generation (RAG)</strong> to deliver context-aware legal answers with document citations.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-6E40C9?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge)
![Llama 3.2](https://img.shields.io/badge/Llama-3.2-blue?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

### 🎥 Project Demonstration

> **Demo GIF**

<p align="center">
<img src="YOUR_GIF_LINK" width="900">
</p>

---

</div>

# 📖 Overview

**Vincenzo** is an AI-powered Legal Research Assistant that enhances legal information retrieval using **Retrieval-Augmented Generation (RAG)**.

Instead of relying solely on the internal knowledge of a Large Language Model, Vincenzo retrieves relevant legal passages from a vector database and uses them as context before generating a response. This enables answers to be grounded in the indexed legal corpus and accompanied by document citations.

The project demonstrates the practical integration of **Large Language Models**, **Semantic Search**, **Vector Databases**, and **Modern Web Technologies** into a modular legal AI application.

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 🤖 Artificial Intelligence

- Retrieval-Augmented Generation (RAG)
- Llama 3.2 via Ollama
- Semantic Search
- Context-Aware Responses
- Prompt Engineering

</td>

<td width="50%">

### ⚖️ Legal Research

- PDF Legal Document Processing
- Source Citations
- Page-Level References
- Multi-Document Retrieval
- Legal Knowledge Base

</td>
</tr>

<tr>
<td>

### ⚡ Backend

- FastAPI
- REST API
- Modular Architecture
- Pydantic Validation
- Scalable Design

</td>

<td>

### 💻 Frontend

- React.js
- Responsive UI
- Modern Chat Interface
- Real-Time Responses

</td>
</tr>
</table>

---

# 🏗 System Architecture

```text
                           User
                             │
                             ▼
                     React Frontend
                             │
                      HTTP REST API
                             │
                             ▼
                    FastAPI Backend
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
          Chroma Vector DB         Llama 3.2 (Ollama)
                 ▲
                 │
         Nomic Embeddings
                 ▲
                 │
          Legal PDF Documents
```

---

# 🧠 RAG Pipeline

```text
📄 Legal Documents
        │
        ▼
📑 PDF Loader
        │
        ▼
✂️ Text Chunking
        │
        ▼
🧠 Generate Embeddings
        │
        ▼
🗂 Store in ChromaDB
        │
        ▼
🔍 Semantic Retrieval
        │
        ▼
📚 Build Context
        │
        ▼
🤖 Llama 3.2
        │
        ▼
⚖️ Legal Answer + Citations
```

---

# 🚀 Technology Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Frontend | React.js |
| Backend | FastAPI |
| AI Framework | LangChain |
| LLM | Llama 3.2 |
| Embedding Model | Nomic Embed Text |
| Vector Database | ChromaDB |
| PDF Loader | PyPDFDirectoryLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| API | REST |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Vincenzo-AI-Lawyer-Assistant/

├── app/
│   ├── config.py
│   ├── get_embedding_function.py
│   ├── prompt.py
│   ├── rag.py
│   ├── models.py
│   ├── main.py
│   └── __init__.py
│
├── scripts/
│   └── populate_database.py
│
├── chroma_db/
│
├── data/
│   └── books/
│
├── frontend/
│
├── requirements.txt
│
└── README.md
```

---

# 📷 Screenshots

## 🏠 Home Page

<p align="center">
<img src="YOUR_HOME_SCREENSHOT" width="900">
</p>

---

## 💬 AI Chat Interface

<p align="center">
<img src="YOUR_CHAT_SCREENSHOT" width="900">
</p>

---

## 📚 Response with Citations

<p align="center">
<img src="YOUR_RESULT_SCREENSHOT" width="900">
</p>

---

# ⚡ Example

## User Query

```text
What is fraud under Section 17 of the Contract Act?
```

## AI Response

```text
According to Section 17 of the Contract Act, fraud includes:

• Suggesting something as true while knowing it is false

• Active concealment of material facts

• Any other act intended to deceive.

Sources

📄 Family Law.pdf — Page 74

📄 IPC.pdf — Page 63
```

---

# 📚 Legal Dataset

The current knowledge base includes legal documents such as:

- Constitution of India
- Indian Penal Code (IPC)
- Code of Criminal Procedure (CrPC)
- Code of Civil Procedure (CPC)
- Consumer Protection Act
- Information Technology Act
- Motor Vehicles Act
- Family Law
- Additional legal reference documents

---

# 📈 Project Highlights

| Capability | Status |
|------------|--------|
| PDF Processing | ✅ |
| Semantic Search | ✅ |
| Retrieval-Augmented Generation | ✅ |
| Source Citations | ✅ |
| Vector Database | ✅ |
| REST API | ✅ |
| React Integration | ✅ |
| Modular Architecture | ✅ |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Vincenzo-AI-Lawyer-Assistant.git

cd Vincenzo-AI-Lawyer-Assistant
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build Vector Database

```bash
python scripts/populate_database.py
```

---

## Run Backend

```bash
python -m app.main
```

---

## Run Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 📡 API Example

### POST

```http
POST /ask
```

Request

```json
{
    "question":"What is fraud under Section 17?"
}
```

Response

```json
{
    "answer":"...",
    "sources":[
        {
            "file":"Family Law.pdf",
            "page":74
        }
    ]
}
```

---

# 🔮 Roadmap

- ✅ Retrieval-Augmented Generation
- ✅ Semantic Search
- ✅ ChromaDB Integration
- ✅ Source Citations
- ✅ React Frontend
- 🔄 Conversation Memory
- 🔄 Hybrid Search (BM25 + Vector Search)
- 🔄 OCR Support
- 🔄 Authentication
- 🔄 Docker Deployment
- 🔄 Cloud Deployment

---

# 👨‍💻 Author & Solo Developer

**AKKi | Akhil Sipahi**

Machine Learning Engineer | Data Scientist

GitHub: https://github.com/akhilbelim94-jpg

LinkedIn: https://linkedin.com/in/akhil-sipahi-5b0079379

---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a Star!

*"Building intelligent systems that combine AI with reliable information retrieval."*

</div>
---

