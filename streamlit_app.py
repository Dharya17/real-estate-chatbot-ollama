import streamlit as st
from agent1 import agent1_flow
from agent2 import ask_tenancy_faq
from router import route_message

# --- Page config and custom CSS ---
st.set_page_config(page_title="PropertyLoop Assistant", layout="centered")

st.markdown("""
    <style>
    html, body {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro", "Helvetica Neue", "Segoe UI", sans-serif;
        background-color: #f9f9f9;
        color: #333;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 8px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #004c99;
    }
    .stTextInput>div>div>input {
        border-radius: 6px;
        padding: 0.5em;
        border: 1px solid #ccc;
    }
    .stFileUploader>div>div {
        background-color: #f1f1f1;
        border-radius: 8px;
        padding: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.title("🏠 PropertyLoop Multi-Agent Assistant")
st.markdown("Upload an image of a property issue or ask a question about your tenancy.")

uploaded_image = st.file_uploader("Upload Property Image", type=["jpg", "jpeg", "png"])
user_text = st.text_input("Ask your question")
location = st.text_input("Enter your location")

if st.button("✨ Generate Response"):
    route = route_message(user_text, has_image=uploaded_image is not None)

    if route == "agent1":
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.read())
        caption, suggestion = agent1_flow("temp_image.jpg")
        st.success("Issue Identified")
        st.markdown(f"** Image Caption:**\n> {caption}")
        st.markdown(f"** Suggestion:**\n> {suggestion}")

    elif route == "agent2":
        response = ask_tenancy_faq(user_text, location=location)
        st.success("Legal Advice")
        st.markdown(f"Response:\n> {response}")

    elif route == "clarify":
        st.warning(" Please clarify: Are you reporting a property issue or asking a tenancy-related question?")
