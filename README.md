# ⚖️ Vincenzo: AI Lawyer Assistant

> An AI-powered Legal Research Assistant that combines **Retrieval-Augmented Generation (RAG)** with **Large Language Models (LLMs)** to answer legal queries using a curated collection of legal documents instead of relying solely on the model's internal knowledge.

---

## 📖 Overview

Vincenzo is an AI-powered legal assistant designed to improve legal information retrieval by grounding responses in actual legal documents.

Instead of generating answers purely from an LLM, Vincenzo first retrieves the most relevant legal passages from a vector database and then uses those passages as context for response generation. This approach helps produce responses that are more relevant, explainable, and traceable to the underlying legal sources.

The project is built using a modern AI stack including **LangChain**, **ChromaDB**, **Ollama**, **Llama 3.2**, **FastAPI**, and **React**.

---

# ✨ Features

- 📚 Retrieval-Augmented Generation (RAG)
- ⚖️ AI-powered legal question answering
- 📄 PDF-based legal document indexing
- 🔍 Semantic search using vector embeddings
- 🧠 Llama 3.2 for response generation
- 🗂 ChromaDB vector database
- 📑 Source document and page citations
- ⚡ FastAPI backend
- 🎨 React frontend
- 🔄 Incremental document indexing
- 📁 Modular project architecture

---

# 🏗 Project Architecture

```text
                        User
                          │
                          ▼
                  React Frontend
                          │
                    REST API Request
                          │
                          ▼
                  FastAPI Backend
                          │
                          ▼
                 Retrieval Pipeline
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
    Chroma Vector DB              Ollama (Llama 3.2)
          ▲
          │
   Nomic Embeddings
          ▲
          │
      Legal PDF Dataset
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | React.js |
| LLM | Llama 3.2 (Ollama) |
| Embeddings | Nomic Embed Text |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Document Loader | PyPDFDirectoryLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| API | REST |
| Version Control | Git & GitHub |

---

# 🧠 RAG Workflow

```text
Legal Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Search (ChromaDB)
      │
      ▼
Retrieve Relevant Documents
      │
      ▼
Build Context
      │
      ▼
Prompt Construction
      │
      ▼
Llama 3.2
      │
      ▼
Answer + Source References
```

---

# 📂 Project Structure

```text
Vincenzo-AI-Lawyer-Assistant/

│
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

# 🚀 How It Works

### 1. Document Processing

- Load legal PDF documents
- Split documents into overlapping chunks
- Generate vector embeddings
- Store embeddings in ChromaDB

---

### 2. User Query

When a user asks a legal question:

- Convert the query into an embedding
- Retrieve relevant legal passages using semantic search
- Build contextual information
- Generate an answer using Llama 3.2
- Return the answer with source references

---

# 📌 Example

### User Question

```
What is fraud under Section 17 of the Contract Act?
```

### Response

```
According to Section 17 of the Contract Act, fraud includes:

• Suggesting something as true while knowing it is false
• Active concealment of material facts
• Any other act intended to deceive

Sources

• Family Law.pdf – Page 74
```

---

# 📚 Current Dataset

The project currently indexes legal documents such as:

- Constitution of India
- Indian Penal Code (IPC)
- Code of Criminal Procedure (CrPC)
- Code of Civil Procedure (CPC)
- Consumer Protection Act
- Motor Vehicles Act
- Information Technology Act
- Family Law
- Additional legal reference material

---

# 💡 Why RAG Instead of Only an LLM?

Traditional LLMs generate responses from learned knowledge, which may not always align with the user's document collection.

Vincenzo uses Retrieval-Augmented Generation (RAG) to ground every response in indexed legal documents before generating an answer. This helps provide answers that are relevant to the available legal corpus and allows the application to return supporting document references.

---

# 🔮 Future Improvements

- Conversation memory
- Multi-turn legal discussions
- Hybrid search (BM25 + Vector Search)
- Cross-encoder reranking
- Citation highlighting
- OCR support for scanned PDFs
- Multilingual legal assistance
- User authentication
- Cloud deployment

---

# 👨‍💻 Author & Solo Developer

**Akhil Sipahi**

Machine Learning Engineer | Data Scientist

GitHub: https://github.com/akhilbelim94-jpg

LinkedIn: https://linkedin.com/in/akhil-sipahi-5b0079379

---

# ⭐ If you found this project useful, consider giving it a star.
