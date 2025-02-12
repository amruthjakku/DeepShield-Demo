import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.error("⚠️ Gemini API key is missing! Please check your .env file.")

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text if response else "No response from AI."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
def chatbot_ui():
    st.title("💬 DeepShield Chatbot")
    user_input = st.text_input("Ask me anything about deepfake detection!")
    if user_input:
        response = get_gemini_response(user_input)
        st.write(f"**🤖 Chatbot:** {response}")

if __name__ == "__main__":
    chatbot_ui()
