import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose a working model
MODEL_NAME = "models/gemini-2.0-flash"  # You can also try: gemini-1.5-pro-latest

# Generic function to query Gemini
def query_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(model_name=MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error from Gemini: {str(e)}"

# Document summarization
def summarize_with_gemini(text: str) -> str:
    prompt = f"Summarize the following document in under 150 words:\n\n{text[:6000]}"
    return query_gemini(prompt)