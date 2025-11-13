import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.embeddings import OllamaEmbeddings #Not used in this script, but imported in case you switch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv
load_dotenv()

# Load Groq and Hugging API Key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Huggingface Embedding
embedding = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2")

# Data Ingetion
loader = PyPDFDirectoryLoader("research_papers")

llm = ChatGroq(groq_api_key =  groq_api_key, model_name = "llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_messages(
    [
    ("system", "You an AI Assistant. Use the given context to answer the questions. "
        "If the answer is not in the context, say 'I dont know'."),
    ("user", "Context:\n {context}\n\nQuestion: {input}")
    ]
)

def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = embedding
        st.session_state.loader = loader
        st.session_state.docs = st.session_state.loader.load() # Document Loader
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
        st.session_state.final_document = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_document,st.session_state.embeddings)
st.title("RAG Document QnA with Groq and Llama")

user_prompt = st.text_input("Enter your question from the document.")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector database is ready!")

import time

if user_prompt and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': user_prompt})
    print(f"Response time : {time.process_time()-start}")

    st.write(response.get("answer", response))


    # With streamlit expander

    with st.expander("Document Similarity Search"):
        for i,doc in enumerate(response.get("context", [])):
            st.write(doc.page_content)
            st.write('-------------------')









