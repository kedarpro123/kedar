import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Skin Care Chatbot", layout="centered")

# Custom styling
st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
            color: #f5f5f5;
        }
        h1 {
            color: #ffb6c1;
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
        }
        .stTextArea textarea {
            background-color: #2a2a3d;
            color: #f5f5f5;
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #ffb6c1;
            color: #1e1e2f;
            border-radius: 8px;
            font-weight: bold;
        }
        .chat-card {
            background-color: #2a2a3d;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for settings
st.sidebar.header("⚙️ Settings")
MODEL_NAMES = ["gpt-4o-mini", "llama-3.3-70b-versatile"]
selected_model = st.sidebar.selectbox("Select Model:", MODEL_NAMES)

system_prompt = st.sidebar.text_area(
    "Define your AI Agent:",
    height=100,
    value="You are a helpful skincare assistant. Provide routines, product suggestions, and general advice, but avoid medical diagnoses."
)

API_URL = "http://127.0.0.1:9999/chat"

# Title
st.title("💎 Skin Care Chatbot 💎")
st.write("Get personalized routines, product suggestions, and skincare tips!")

# User query
user_query = st.text_area("💬 Ask your skincare question:", height=120, placeholder="e.g., Best routine for oily skin?")

# Ask button
if st.button("✨ Get Advice ✨"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": "OpenAI",
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
                st.markdown('<div class="chat-card">', unsafe_allow_html=True)
                st.subheader("🌿 Skincare Tip 🌿")
                if "reply" in response_data:
                    st.write(response_data["reply"])
                else:
                    st.write(response_data)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"Backend error: {response.status_code}")
           









