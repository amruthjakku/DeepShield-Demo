import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.error("⚠️ Gemini API key is missing! Please check your .env file.")

# Function to generate response from Gemini AI
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text if response else "No response from AI."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle file upload and analysis
def analyze_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "Size": uploaded_file.size}
        st.write(file_details)
        
        # Save file locally
        file_path = f"./uploads/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✅ File {uploaded_file.name} uploaded successfully!")
        st.write("🔍 Analyzing file for deepfake detection...")
        
        # (Call deepfake detection model here)
        analysis_result = "⚠️ Deepfake detected!"  # Placeholder for AI model output
        st.write(f"**Analysis Result:** {analysis_result}")

# Streamlit UI
st.set_page_config(page_title="DeepShield Chatbot", layout="wide")

st.sidebar.title("Chat with AI-Powered Deepfake Detection Bot!")
st.title("💬 DeepShield Chatbot")

# Chatbox
user_input = st.text_input("Ask me anything about deepfake detection!")
if user_input:
    response = get_gemini_response(user_input)
    st.write(f"**🤖 Chatbot:** {response}")

# File Upload Section
st.subheader("📂 Upload an Image/Video for Deepfake Detection")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "mp4"])
if uploaded_file:
    analyze_uploaded_file(uploaded_file)
