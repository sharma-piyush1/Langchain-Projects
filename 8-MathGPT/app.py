import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain 
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Set up the streamlit app

st.set_page_config(page_title="Text to Math Problem solbver and Data Search Assistant", page_icon="🦜", layout="centered")
st.title("Text to MAth Problem with OpenAI GPT")


groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

llm=ChatGroq(model="openai/gpt-oss-120b", groq_api_key=groq_api_key)

# Initializeing the tool

wikipedia_wrapper= WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the internet to find the various topics mentioned."
)

# Initialize the Math tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answring math related question. Only inout mathematical expression needs to be provided."
)

prompt = """
You are an agent that solves users' mathematical questions. 
Logically arrive at the solution and provide a detailed explanation, 
showing steps clearly for the question below.

Question: {question}
Answer:
"""

prompt_template= PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# Combine all the tool into chain

chain=LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool= Tool(
    name="Reasoning",
    func=chain.run,
    description="A tool for answering logic-based and reasonhg question."
)

# Initialize the agents

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {'role':"assistant", "content": "Hi, I am your Chatbot that will answer all your math problem."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


# function to generate the response

# Lets start the interaction

question= st.text_area("Enter your question:", " ")

if st.button("Find my answer"):
    if question:
        with st.spinner("Generating response..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = ""
            try:
                response = assistant_agent.run(question, callbacks=[st_cb])
            except Exception as e:
                st.error(f"Error: {e}")

            if response:
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.write('### Response:')
                st.success(response)

            

    else:
        st.warning("Please enter the question")
        





