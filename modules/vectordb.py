# Load Chroma DB
from langchain_community.vectorstores import Chroma

def load_vectordb():
    print("Loading vector database...")
    vectordb = Chroma(
        persist_directory="nutrition_db",
        embedding_function=None  # Embeddings already stored in DB
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 20})
    return retriever
