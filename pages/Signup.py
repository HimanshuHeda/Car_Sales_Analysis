import streamlit as st
import re
from utils import signup_user

st.title("📝 Sign Up")

username = st.text_input("Choose a username")
password = st.text_input("Choose a password", type="password")

# Strong password rules
def is_strong_password(pw):
    return (
        len(pw) >= 8 and
        any(c.islower() for c in pw) and
        any(c.isupper() for c in pw) and
        any(c.isdigit() for c in pw) and
        any(c in "!@#$%^&*()-_+=" for c in pw)
    )

if st.button("Create Account"):
    if not username.strip() or not password:
        st.error("All fields are required.")
    elif not is_strong_password(password):
        st.error("Password must be at least 8 characters long and include uppercase, lowercase, a number, and a symbol.")
    else:
        if signup_user(username.strip(), password):
            st.success(f"Account for '{username}' created successfully!")
            st.info("Please login to continue.")
            st.switch_page("pages/Login.py")
        else:
            st.error("Username already exists. Try a different one.")
