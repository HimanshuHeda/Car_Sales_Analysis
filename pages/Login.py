import streamlit as st
from utils import login_user

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Create two columns for side-by-side buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Login"):
        if login_user(username, password):
            st.success(f"Welcome, {username}!")
            st.switch_page("pages/ImageAnalyzer.py")
        else:
            st.error("Invalid credentials")

with col2:
    if st.button("Register"):
        st.switch_page("pages/Signup.py")
