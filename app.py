import streamlit as st
from modules.llm import load_llm
from modules.vectordb import load_vectordb
from modules.ragchain import build_chain

#Page Config
st.set_page_config(
    page_title="Healthy Diet Assistant",
    page_icon="🥗",
    layout="centered"
)

# BEAUTIFUL CUSTOM CSS
st.markdown(
    """
    <style>
    /* Entire background gradient */
    body {
        background: linear-gradient(135deg, #E8F5E9 0%, #E3F2FD 100%) !important;
    }

    /* Center app */
    .main {
        max-width: 900px;
        margin: 0 auto;
        padding-top: 20px;
    }
    /* Title with gradient text */
    .title {
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #2E7D32, #66BB6A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: -10px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #444;
        margin-bottom: 40px;
    }
    /* Chat response box */
    .response-box {
        background-color: #F0FFF4;
        padding: 18px;
        border-radius: 12px;
        border-left: 6px solid #2E7D32;
        font-size: 17px;
        line-height: 1.6;
    }

   /* User message bubble */
    .user-bubble {
        background: #C8E6C9;
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 12px;
        width: fit-content;
        max-width: 85%;
        font-size: 17px;
    }
    /* AI message bubble */
    .ai-bubble {
        background: #F1F8E9;
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 12px;
        border-left: 5px solid #2E7D32;
        width: fit-content;
        max-width: 85%;
        font-size: 17px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }

    
    /* Stylish button */
    div.stButton > button {
        background: linear-gradient(90deg, #2E7D32, #66BB6A);
        color: white;
        padding: 0.7rem 1.4rem;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        transition: 0.2s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #1B5E20, #43A047);
        transform: scale(1.02);
    }

    /* Input box styling */
    .stTextInput > div > div > input {
        padding: 16px;
        border: 2px solid #A5D6A7;
        border-radius: 12px;
        font-size: 18px;
    }


    </style>
    """,
    unsafe_allow_html=True
)

st.title("🥗 Healthy Diet Assistant")
st.write("Ask any nutrition-related question based on WHO, USDA, Harvard, and Diabetes Canada guidelines.")

# Load components
with st.spinner("Loading model and vector database..."):
    llm = load_llm()
    retriever = load_vectordb()
    rag_chain = build_chain(retriever, llm)

# input box
user_query = st.text_input("Ask a nutrition question:")

if st.button("Get Answer"):
    if not user_query.strip():
        st.warning("Please type a question.")
    else:
        with st.spinner("Thinking..."):
            response = rag_chain.invoke({"question": user_query})

        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
