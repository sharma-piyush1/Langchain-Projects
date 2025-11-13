# Search Engine Chatbot

Lightweight Streamlit demo that combines a search/indexing layer with a generative LLM to answer user queries using retrieved sources.

## Contents
- app.py — main Streamlit application (UI + search + LLM pipeline)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (not checked in)
- data/ — optional source documents or crawl outputs
- vectorstore/ — optional persisted index
- README.md — this file

## Features
- Search or index documents (local files, web crawl, or custom source)
- Retrieval + generation (RAG) to produce answers grounded in retrieved documents
- Sidebar controls for model, temperature, and token limits
- Optional LangChain/LangSmith tracing

## Prerequisites
- Windows
- Python 3.9+
- pip
- (Optional) Search/index tooling (FAISS, Chroma, Whoosh, or external search API)
- LLM access (OpenAI, Ollama, Groq, or other provider used in app)

## Quick start

1. Open PowerShell and create/activate a venv:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Create a `.env` with required keys (example):
```
LANGCHAIN_API_KEY=your_langchain_key
OPENAI_API_KEY=your_openai_key       # if using OpenAI embeddings/LLM
SEARCH_API_KEY=your_search_api_key   # if using external search service
VECTORSTORE_PATH=./vectorstore
```

## Run
From the project folder:
```powershell
streamlit run "app.py"
```

## Usage
- Ingest or point the app to your data source (if ingestion is required).
- Use the sidebar to configure model and generation parameters.
- Enter queries in the UI to receive answers with supporting retrieved context (if enabled).

## Troubleshooting
- No search results: verify the index was created or the search API/key is correct.
- No LLM response: check API keys, model names, and quotas.
- Missing packages: ensure requirements.txt matches the code imports.

## Security
- Do not commit `.env` or API keys to version control.
- Limit max tokens and monitor usage to control costs.

## License
Provided as-is for learning and experimentation.
