# MathGPT

Streamlit demo that uses a language model to solve and explain mathematical problems (algebra, calculus, numeric reasoning). Designed as a compact educational/utility project in the Udemy Gen AI / LangChain series.

## Contents
- app.py — main Streamlit application (UI + model invocation)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (do not commit)
- README.md — this file

## Features
- Natural-language math questions -> worked solutions and explanations
- Supports step-by-step reasoning and formatted math output (LaTeX/Markdown)
- Sidebar controls for model, temperature, and token limits
- Optional tracing via LangChain / LangSmith

## Prerequisites
- Windows
- Python 3.9+
- pip

## Setup (PowerShell)
1. Create & activate a virtual environment:
```powershell
cd "D:\Udemy Gen AI\Langchain Projects\8-MathGPT"
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Create a `.env` with required keys (example):
```
OPENAI_API_KEY=your_openai_key_here
LANGCHAIN_API_KEY=your_langchain_key_here    # optional, for tracing
```
Do not commit `.env`.

## Run
From the project folder:
```powershell
streamlit run "app.py"
```

## Usage
- Enter a math question in plain English (for example: "Integrate x^2 sin(x) dx" or "Solve 2x+3=7 and show steps").
- Adjust model and generation parameters in the sidebar if available.
- View the solution and step-by-step explanation rendered in the app.

## Notes & Troubleshooting
- If results are incorrect, lower temperature for more deterministic outputs or refine the prompt/template.
- For LaTeX rendering issues, confirm the app uses Streamlit's markdown/MathJax rendering.
- Ensure API keys are valid and have sufficient quota.

## Security & Best Practices
- Keep API keys out of version control.
- Do not use generated SQL or code from the model in production without review.

## License
Provided as-is for learning and experimentation.
```// filepath: D:\Udemy Gen AI\Langchain Projects\8-MathGPT\README.md
# MathGPT

Streamlit demo that uses a language model to solve and explain mathematical problems (algebra, calculus, numeric reasoning). Designed as a compact educational/utility project in the Udemy Gen AI / LangChain series.

## Contents
- app.py — main Streamlit application (UI + model invocation)
- requirements.txt — Python dependencies (create if missing)
- .env — environment variables (do not commit)
- README.md — this file

## Features
- Natural-language math questions -> worked solutions and explanations
- Supports step-by-step reasoning and formatted math output (LaTeX/Markdown)
- Sidebar controls for model, temperature, and token limits
- Optional tracing via LangChain / LangSmith

## Prerequisites
- Windows
- Python 3.9+
- pip

## Setup (PowerShell)
1. Create & activate a virtual environment:
```powershell
cd "D:\Udemy Gen AI\Langchain Projects\8-MathGPT"
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Create a `.env` with required keys (example):
```
OPENAI_API_KEY=your_openai_key_here
LANGCHAIN_API_KEY=your_langchain_key_here    # optional, for tracing
```
Do not commit `.env`.

## Run
From the project folder:
```powershell
streamlit run "app.py"
```

