# PDF Query with AstraDB

Streamlit demo that ingests PDF documents, builds a vector index, and answers user queries using a Retrieval‑Augmented Generation (RAG) pipeline with AstraDB (DataStax Astra) as the vector/document store.

## Contents
- app.py — main Streamlit app (ingest PDFs, query UI)
- ingest.py (optional) — PDF ingestion / indexing utility
- requirements.txt — Python dependencies
- .env — environment variables (not checked in)
- data/ — sample PDFs (optional)
- vectorstore/ or persisted index — local cache (optional)

## Features
- Upload or point to PDF files for indexing
- Extract text, chunk documents, compute embeddings
- Store/retrieve vectors and metadata in AstraDB (or local fallback)
- Use retrieved context to generate grounded answers with an LLM
- Sidebar controls for model and generation parameters

## Prerequisites
- Windows
- Python 3.9+
- pip
- DataStax Astra DB account with an Astra DB key or connection details (for vector storage)
- LLM provider credentials for embeddings and/or generation (OpenAI, Hugging Face, etc.)

## Environment variables (.env)
Create a .env in the project folder with required values. Example:
```
ASTRA_DB_ID=your_astra_db_id
ASTRA_DB_REGION=your_astra_region
ASTRA_DB_KEYSPACE=your_keyspace
ASTRA_APPLICATION_TOKEN=your_application_token
EMBEDDINGS_PROVIDER=openai               # or huggingface, etc.
OPENAI_API_KEY=your_openai_key           # if using OpenAI embeddings/LLM
LANGCHAIN_API_KEY=your_langchain_key     # optional, for LangSmith tracing
VECTORSTORE_TABLE=pdf_vectors            # optional, table/collection name in Astra
```
Do not commit .env to source control.

## Setup (PowerShell)
1. Create & activate a virtual environment:
```powershell
cd "D:\Udemy Gen AI\Langchain Projects\10-PDFquery with AstraDB"
python -m venv .venv
.venv\Scripts\Activate.ps1
```
2. Install dependencies:
```powershell
pip install -r requirements.txt
```

## Ingest PDFs
- If the project includes an ingestion script:
```powershell
python ingest.py --data_dir "./data" --use_astra True
```
- Or use the app UI to upload PDFs and run indexing.

## Run the App
```powershell
streamlit run "app.py"
```