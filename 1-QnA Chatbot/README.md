# QnA Chatbot with OpenAI

Lightweight Streamlit app that prompts OpenAI via LangChain to answer user questions.

## Contents
- [1-QnA Chatbot/app.py](1-QnA Chatbot/app.py) — main app file
- [1-QnA Chatbot/.env](1-QnA Chatbot/.env) — environment variables (not checked in)

## Quick start

1. Install dependencies:
```sh
pip install -r "1-QnA Chatbot/requirements.txt"

2. Create or update .env in the folder [1-QnA Chatbot/.env](1-QnA Chatbot/.env) with:

LANGCHAIN_API_KEY=your_langchain_key_here

3. Run the app:
streamlit run "1-QnA Chatbot/app.py"

4. In the app sidebar paste your OpenAI API key (the app uses the sidebar input for openai.api_key).

How it works
The app UI is implemented in [1-QnA Chatbot/app.py](1-QnA Chatbot/app.py).
The prompt template used to format queries is the [prompt](1-QnA Chatbot/app.py) variable in the same file.
The request/response logic is encapsulated in the [generate_response](1-QnA Chatbot/app.py) function.
Configuration
Sidebar options:

OpenAI API Key (required)
Model selection (e.g. gpt-5-2025-08-07, gpt-5-mini-2025-08-07, gpt-5-nano-2025-08-07)
Temperature and max tokens sliders
LangSmith tracing is enabled via environment variables set in the app:

LANGCHAIN_API_KEY (from .env)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=QnA Chatbot

Notes & tips
The UI sends the API key from the sidebar input to the app at runtime (it is not read from .env for OpenAI).
Edit the prompt template in [prompt](1-QnA Chatbot/app.py) to customize system instructions.
For debugging, check Streamlit logs and ensure your OpenAI key has sufficient quota.
Troubleshooting
If you see import errors, confirm the correct versions in 1-QnA Chatbot/requirements.txt.
If no response appears, confirm the OpenAI API key entered in the sidebar is valid.