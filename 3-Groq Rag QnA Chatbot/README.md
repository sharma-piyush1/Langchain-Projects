# Groq RAG QnA Chatbot

Lightweight Streamlit app that implements a Retrieval-Augmented Generation (RAG) QnA using Groq (inference) for LLM responses and a local or cloud vector store for retrieval. Designed as a demo project in the Udemy "Gen AI / LangChain" series.

## Contents
- app.py — main Streamlit application (RAG pipeline + UI)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (not checked in)
- data/ — optional folder for source documents to index
- README.md — this file

(Actual filenames may vary; adjust paths if your project layout differs.)

## Features
- Upload or point to documents to build a retrieval index
- Embed documents and store vectors in chosen vector store
- Use Groq model for generation of answers based on retrieved context
- Simple Streamlit UI to ask questions and tune generation parameters

## Prerequisites
- Windows machine
- Python 3.9+
- pip
- (Optional) Groq account / local Groq runtime if using on-prem inference
- Any required vector store (FAISS, Chroma, Milvus, etc.) depending on project implementation

## Setup

1. Open PowerShell and create/activate a virtual environment:
```powershell
cd "D:\Udemy Gen AI\Langchain Projects\3-Groq Rag QnA Chatbot"
python -m venv .venv
.venv\Scripts\Activate.ps1

2. Install dependencies:
pip install -r [requirements.txt](http://_vscodecontentref_/0)

3. Create a .env file in the project root and add required keys. Typical variables:
LANGCHAIN_API_KEY=your_langchain_key_here          # optional, for LangSmith tracing
GROQ_API_KEY=your_groq_api_key_here                # if using Groq cloud
OPENAI_API_KEY=your_openai_api_key_here            # if embeddings or fallback use OpenAI
VECTORSTORE_PATH=./vectorstore                      # path for local vector db (if applicable)

Do not commit .env to source control.

Usage
(Optional) Prepare and ingest documents into the vector store. This project may include an ingestion utility or ingest on first run.

Run the Streamlit app:
streamlit run "app.py"

3. In the app:
    Configure API keys or paste them in the sidebar if the app requests them.
    Select model / retrieval options, adjust temperature and max tokens.
    Ask a question and view the RAG-powered response and retrieved context (if enabled).

Configuration notes
    If using a local vector store (FAISS/Chroma), ensure the embedding model is configured (OpenAI, Hugging Face, etc.).
    If Groq is used for generation, confirm model name and region in app config or environment variables.
    LangChain tracing: enable via LANGCHAIN_API_KEY and LANGCHAIN_TRACING_V2 or LANGCHAIN_TRACKING env vars if you want LangSmith traces.

Troubleshooting
    No response: check API keys, internet connectivity, and that any daemon/service (e.g., Groq runtime) is running.
    Missing packages: re-check requirements.txt and installed versions.
    Indexing errors: ensure document formats are supported and that embeddings are being produced.

Security & Best Practices
    Keep API keys out of version control (.gitignore .env).
    Limit max tokens and monitor usage to control costs.
    Sanitize user inputs if exposing the app publicly.