from langchain_google_genai import ChatGoogleGenerativeAI
from modules.config import load_api_key

#load llm
def load_llm():
    api_key = load_api_key()
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.6
    )
    return llm