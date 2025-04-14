import streamlit as st
from pathlib import Path
import base64

# Set page config
st.set_page_config(page_title="Home", layout="wide")

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()  # Correct usage
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
# Inject custom CSS for background image
st.markdown(
    f"""
    <style>
    .centered {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
        font-size: 2rem;
        background: rgba(0, 0, 0, 0.5);
        padding: 2rem;
        border-radius: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Centered content
set_background("./car_bg.jpg")
st.markdown("## 🚗 Welcome to Car Sales Dashboard")
if st.button("🔐 Login"):
    st.switch_page("pages/Login.py")
