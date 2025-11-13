# SQL Chatbot

Streamlit demo that connects a language model to a SQL database for querying and conversational access to data.

## Contents
- app.py — main Streamlit app
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (do not commit)
- README.md — this file

## Features
- Natural-language to SQL / SQL-to-natural-language conversion via an LLM
- Execute read-only queries against a configured database
- Sidebar controls for model, temperature, and max tokens
- Optional LangChain tracing via LangSmith

## Prerequisites
- Windows
- Python 3.9+
- pip
- A SQL database (SQLite, Postgres, MySQL, etc.) and a read-only connection for the app

## Setup (PowerShell)
1. Create & activate venv:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Create a `.env` with required variables (example):
```
DATABASE_URL=sqlite:///./data.db        # or postgres://user:pass@host:port/db
OPENAI_API_KEY=your_openai_key_here     # or other LLM provider key
LANGCHAIN_API_KEY=your_langchain_key    # optional, for tracing
```

## Run
From the project folder:
```powershell
streamlit run "app.py"
```

## Usage
