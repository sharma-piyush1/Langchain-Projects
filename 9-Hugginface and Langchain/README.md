# Hugging Face + LangChain Demo

Small demo integrating Hugging Face models (local or Hub) with LangChain utilities to build retrieval, chat, or generation pipelines.

## Contents
- app.py — main Streamlit app or script (model + LangChain pipeline)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (do not commit)
- data/ — optional source documents or assets
- README.md — this file

## Features
- Use Hugging Face Hub or local transformer models for embeddings / generation
- Plug-and-play with LangChain prompt templates, chains, and vector stores
- Support for local inference (transformers/accelerate) or HF Inference API
- Options for retrieval (FAISS/Chroma) and RAG-style Q&A

## Prerequisites
- Windows
- Python 3.9+
- pip
- (Optional) GPU and accelerate for local model inference
- Hugging Face account or API token if using Hub/inference API

## Environment variables (.env)
- HUGGINGFACEHUB_API_TOKEN=your_hf_token
- LANGCHAIN_API_KEY=your_langchain_key (optional, for LangSmith tracing)
- MODEL_NAME=your_model_name (optional default)

Do not commit .env to source control.

## Quick setup (PowerShell)
1. Create & activate venv:
```powershell
cd "D:\Udemy Gen AI\Langchain Projects\9-Hugginface and Langchain"
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Populate `.env` with required keys.

## Running
- If the project uses Streamlit:
```powershell
streamlit run "app.py"
```
- If it is a plain script:
```powershell
python "app.py"
```
