import requests
import json
import gradio as gr

# Ollama local endpoint
url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

def generate_response(message, history):
    """
    message: latest user message
    history: full chat history as [(user, assistant), ...]
    """
    # Combine chat history into a single prompt
    conversation = ""
    for user_msg, bot_msg in history:
        conversation += f"User: {user_msg}\nAssistant: {bot_msg}\n"
    conversation += f"User: {message}\nAssistant:"

    data = {
        "model": "codeguru",
        "prompt": conversation,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 256
            }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "No response field found.")
        else:
            return f"⚠️ API Error: {response.status_code}\n{response.text}"
    except Exception as e:
        return f"❌ Connection Error: {str(e)}"

# Gradio Chat Interface
chatbot = gr.ChatInterface(
    fn=generate_response,
    title="💬 Local CodeGuru Assistant",
    description="Chat with your local LLM running on Ollama. Powered by Gradio.",
    theme="soft",
    examples=[
        ["Explain the difference between Python list and tuple"],
        ["Write a Python function to reverse a string"],
        ["Give me 3 project ideas using LangChain"]
    ]
)

# Launch with shareable link if needed
chatbot.launch(share=False)
