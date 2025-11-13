# Assistant with CodeLlama

Streamlit demo that builds a coding assistant using CodeLlama (local or Hub) and LangChain. Designed for code generation, explanation, and simple code-edit tasks.

## Contents
- app.py — main Streamlit app (chat/code assistant UI)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (do not commit)
- data/ — example prompts, snippets, or test files (optional)
- README.md — this file

## Features
- Chat-style coding assistant (generate, explain, refactor code)
- Option to use local CodeLlama model or Hugging Face Inference/Hub
- LangChain prompt templates and chains for structured prompts
- Sidebar controls for model selection, temperature, and token limits

## Prerequisites
- Windows
- Python 3.9+
- pip
- (Optional) GPU & appropriate drivers for local model inference
- Hugging Face account/token if using Hub/inference API

## Environment variables (.env)
Typical variables: