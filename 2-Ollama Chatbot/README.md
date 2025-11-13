# Ollama QnA Chatbot

Lightweight Streamlit app that uses LangChain + Ollama to answer user questions.

## Files
- app.py — main Streamlit app

## Requirements
- Python 3.9+
- pip packages (example):
  - streamlit
  - langchain-core
  - langchain-community
  - python-dotenv

Create a `requirements.txt` with the packages used in your environment.

## Setup

1. Install dependencies
   ```powershell
   pip install -r requirements.txt

2. (Optional) Create a .env in the folder with tracking key(s) if you use LangSmith:

LANGCHAIN_API_KEY=your_langchain_key_here

3. Ensure Ollama is available:

    Install Ollama and run the Ollama daemon (if using local Ollama).
    Confirm the model names in the app (e.g. llama3.2:latest, gemma3:latest) are installed/available to Ollama.

Run
From the project folder:
streamlit run "app.py"

Usage
Select an Ollama model from the sidebar.
Adjust Temperature and Max Tokens.
Type a question in the main input and submit to get a response.
Implementation notes
The app builds a ChatPromptTemplate and pipes it through the Ollama LLM and a StrOutputParser:

prompt messages are defined in app.py.
generate_response(question, engine, temperature, max_tokens) invokes the chain.
LangChain tracing is enabled via environment variables set in app.py:

LANGCHAIN_API_KEY (from .env)
LANGCHAIN_TRACKING = true
LANGCHAIN_PROJECT = "Ollama QnA Chatbot"

Troubleshooting
No response: ensure Ollama daemon is running and the selected model is installed.
Import errors: confirm package versions in requirements.txt.
Tracing not visible: verify LANGCHAIN_API_KEY and tracing env values.
