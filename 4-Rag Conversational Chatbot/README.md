# RAG Conversational Chatbot

Streamlit demo implementing a conversational Retrieval-Augmented Generation (RAG) chatbot using LangChain. The app supports multi-turn chat, document retrieval (vector store), and configurable LLM settings.

## Contents
- app.py — main Streamlit app (conversation + retrieval logic)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (do not commit)
- data/ — source documents (optional)
- vectorstore/ — persisted vector index (optional)
- README.md — this file

## Features
- Multi-turn conversational interface with context memory
- Document ingestion and retrieval (FAISS / Chroma / other)
- Configurable LLM model, temperature, and max tokens
- LangChain tracing support (LangSmith) via env vars

## Prerequisites
- Windows
- Python 3.9+
- pip
- (Optional) Local vector store dependencies (FAISS/Chromadb)
- LLM access (OpenAI, Ollama, Groq, or other supported provider)

## Quick setup
1. Open PowerShell and create & activate a venv:
```powershell
cd "D:\Udemy Gen AI\Langchain Projects\4-Rag Conversational Chatbot"
python -m venv .venv
.venv\Scripts\Activate.ps1

2. Install dependencies:
pip install -r [requirements.txt](http://_vscodecontentref_/0)

3. Create a .env with required keys (example):
LANGCHAIN_API_KEY=your_langchain_key
OPENAI_API_KEY=your_openai_key         # if using OpenAI embeddings/LLM
VECTORSTORE_PATH=./vectorstore

Run
From the project folder:

streamlit run "app.py"

Usage
    Load or ingest documents (if the app provides an ingestion step).
    Start a conversation in the UI; the bot uses retrieved context plus conversation history to answer.
    Adjust model, temperature, and token limits in the sidebar.
Notes & troubleshooting

    Ensure the vector store is built before querying; re-ingest if retrieval returns no results.
    If using local services (Ollama, Groq), confirm daemons are running and models are installed.
    Enable LangChain tracing by setting LANGCHAIN_API_KEY and LANGCHAIN_TRACING_V2=true.
    Keep .env out of version control.