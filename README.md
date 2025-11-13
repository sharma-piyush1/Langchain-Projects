# LangChain Projects (Udemy Gen AI)

Collection of small LangChain + LLM demo projects used for learning and experimentation.

## Contents
Each subfolder is a standalone demo. Brief summary:
- 1-QnA Chatbot — OpenAI + LangChain Streamlit Q&A
- 2-Ollama Chatbot — Ollama + LangChain Streamlit Q&A
- 3-Groq Rag QnA Chatbot — RAG with Groq for generation
- 4-Rag Conversational Chatbot — Multi-turn RAG conversational agent
- 5-Search Engine Chatbot — Search + RAG Q&A
- 6-SQL Chatbot — Natural language to SQL + execution (read-only)
- 7-Text Summarization — Text/file summarization demo
- 8-MathGPT — Math problem solver + explanations
- 9-Hugginface and Langchain — Hugging Face model integrations
- 10-PDFquery with AstraDB — PDF ingestion + vector store (AstraDB)
- 11-Assistant with Codellama — Code assistant using CodeLlama

## Prerequisites
- Windows
- Python 3.9+
- pip
- (Optional) Ollama, Groq, local models, or DB services used by specific projects

## Quick setup (recommended, PowerShell)
1. Create a repo-level virtual environment (optional per-project venvs are fine):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

2. Install dependencies per project:

pip install -r [requirements.txt](http://_vscodecontentref_/0)

Environment variables
Create a .env in each project folder when needed. Common variables:

    OPENAI_API_KEY
    LANGCHAIN_API_KEY
    HUGGINGFACEHUB_API_TOKEN
    ASTRA_* (for AstraDB)
    GROQ_API_KEY
    Do not commit .env files. Add them to .gitignore.

Running a project
Most demos are Streamlit apps. From the project folder:
streamlit run "app.py"

Follow the app sidebar prompts for API keys, model selection, and parameters.

Project notes
    Verify required local services (Ollama, Groq, local model servers) are running before launching related apps.
    For retrieval projects, ingest documents / build the index before querying.
    Use read-only DB credentials for the SQL Chatbot and validate generated SQL before executing in production.

Repository maintenance
    Each project should include a requirements.txt and its own README.md (already provided in subfolders).
    A root .gitignore should exclude virtualenvs, .env, editor files, model weights, caches, and large data.

Troubleshooting
    Import errors: install packages listed in the project's requirements.txt.
    No responses: check API keys, service daemons, and model availability.
    Indexing/retrieval issues: re-run ingestion and confirm vector store persistence.


