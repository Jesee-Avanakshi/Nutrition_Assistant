from dotenv import load_dotenv
import os

# Load API key

def load_api_key():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found")
    return api_key
