import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Streamlit App

st.set_page_config(page_title="LangChain Summarizer", page_icon="🦜", layout="centered")

st.markdown("""
    <style>
            
    /* Main page background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #f8f9fa;
        font-family: 'Poppins', sans-serif;
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #1a1d23;
        color: #f8f9fa;
    }

    /* Fix Deploy & Settings buttons visibility */
    header[data-testid="stHeader"] {
        background: rgba(15, 32, 39, 0.6);
        backdrop-filter: blur(8px);
    }

    /* Force white icons for clarity */
    button[kind="header"] svg {
        fill: white !important;
    }

    /* Input boxes */
    .stTextInput>div>div>input {
        border-radius: 8px;
        background-color: #f8f9fa;
        color: #000000;
    }

    /* Buttons */
    .stButton>button {
        background-color: #10a37f;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0d8a6d;
    }

    /* Divider color */
    hr {
        border: 1px solid #10a37f;
    }

    /* Scrollbar customization */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #10a37f;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)




st.markdown("""
    <h2 style='text-align:center; color:#10a37f;'>🦜 LangChain Summarizer</h2>
    <p style='text-align:center;'>Summarize YouTube videos or websites using Llama 3.3 🚀</p>
""", unsafe_allow_html=True)

st.divider()

# Get the Groq API key and URl to be summarize

with st.sidebar:
    st.header("🔐 API Settings")
    groq_api_key = st.text_input("Enter your Groq API Key", type="password", placeholder="sk-...")
    st.divider()
    st.caption("💡 Tip: Get your free API key from Groq Cloud.")

st.markdown("""
    <style>
    /* Make all sidebar text labels white */
    .css-1d391kg label, /* text input labels */
    .css-1d391kg span, /* placeholder / small text */
    .stTextInput>div>label {
        color: white !important;
    }

    /* Make header and caption text white */
    .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar p, .stSidebar div {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)



generic_url = st.text_input("🔗 Paste URL here", placeholder="https://www.youtube.com/watch?v=...")



prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}
"""

prompt=PromptTemplate(template=prompt_template, input_variables=["text"])

if st.button("Summarize the content from YT or Website"):
    # Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can may be a YT video URL or Website URL.")
    else:
        try: 
            with st.spinner("Summarizing..."):
                llm = ChatGroq(groq_api_key=groq_api_key, model = "llama-3.3-70b-versatile") 

                # loading the website or YT video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()

                 # Split large text into smaller chunks
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
                split_docs = text_splitter.split_documents(docs)   

                # Chain from summarization

                chain=load_summarize_chain(
                    llm=llm,
                    chain_type="stuff",
                    prompt=prompt
                )
                 # Summarize each chunk and combine results
                summaries = []
                for i, doc in enumerate(split_docs):
                    summaries.append(chain.run([doc]))

                final_summary = "\n\n".join(summaries)

                
                st.markdown("""
                    <div style='background-color:#1e293b; padding:15px; border-radius:10px; color:#e2e8f0; margin-top:20px;'>
                    <h4>📄 Summary:</h4>
                    <p>{}</p>
                    </div>
                    """.format(final_summary.replace("\n", "<br>")), unsafe_allow_html=True)
                st.download_button("⬇️ Download Summary", final_summary, "summary.txt")



        except Exception as e:
            st.exception(f"Exception:{e}")



