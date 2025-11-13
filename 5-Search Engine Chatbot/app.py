import streamlit as st
from langchain_groq import ChatGroq
from duckduckgo_search import DDGS
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
load_dotenv()

# Arxiv and Wikipedia tool
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max = 250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results = 1, doc_content_chars_max = 250)
arxiv = ArxivQueryRun(api_wrapper = api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name="Search")

st.title("Chatbot with Search and Memory - Langchain, Groq")

"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# Settings for Sidebar

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter the Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi I am chatbot who can search the web. How can I help you?"}

    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt:= st.chat_input(placeholder="What is the Machine Learning"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key = api_key, model_name = "llama-3.1-8b-instant", streaming = True)

    tools = [wiki, arxiv, search]

    # Create Buffer memory
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
    memory = st.session_state.memory

    search_agent =  initialize_agent(tools, llm, agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, memory=memory, handle_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container())
        response= search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": prompt})
        st.write(response) 
          

