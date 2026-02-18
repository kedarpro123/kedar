import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Skin Care Chatbot", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f6f2;
        }
        h1 {
            color: #d17b88;
            text-align: center;
        }
        .stTextArea textarea {
            background-color: #fff8f7;
        }
        .stButton>button {
            background-color: #d17b88;
            color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌸 Your Skin Care Companion 🌸")
st.write("Ask me about routines, products, or general skin care advice!")

# System prompt (pre-filled for skincare)
system_prompt = st.text_area(
    "Define your AI Agent:", 
    height=70, 
    value="You are a helpful skincare assistant. Provide routines, product suggestions, and general advice, but avoid medical diagnoses."
)

# Model selection
MODEL_NAMES = ["gpt-4o-mini", "llama-3.3-70b-versatile"]
selected_model = st.selectbox("Select Model:", MODEL_NAMES)

# User query
user_query = st.text_area("💬 Enter your skincare question:", height=150, placeholder="e.g., How do I treat dry skin?")

API_URL = "http://127.0.0.1:9999/chat"

# Ask button
if st.button("✨ Get Advice ✨"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": "OpenAI",  # or Groq if you want
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": False
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("🌿 Skincare Tip 🌿")
                if "reply" in response_data:
                    st.success(response_data["reply"])
                else:
                    st.success(response_data)
        else:
            st.error(f"Backend error: {response.status_code}")
