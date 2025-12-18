from dotenv import load_dotenv
import os
import streamlit as st

# Load API key

def load_api_key():
    load_dotenv()
    local_key = os.getenv("GOOGLE_API_KEY")
    cloud_key = st.secrets.get("GOOGLE_API_KEY")
    api_key = cloud_key or local_key
    if not api_key:
        raise ValueError("API key not found")
    return api_key
