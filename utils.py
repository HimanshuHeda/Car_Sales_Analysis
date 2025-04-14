import streamlit as st
import json
from pathlib import Path
import cv2
import numpy as np
import hashlib

USER_FILE = Path("users.json")

# Load users from file
def load_users():
    if USER_FILE.exists():
        try:
            with open(USER_FILE, "r") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
        except json.JSONDecodeError:
            pass
    return {}

# Save users to file
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def login_user(username, password):
    users = load_users()
    if username in users and users[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        return True
    return False

def signup_user(username, password):
    users = load_users()
    if username in users:
        return False  # Already exists
    users[username] = password
    save_users(users)
    return True

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup_user(username, password):
    # Hash before saving
    hashed_pw = hash_password(password)

# Image Analysis Functions
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_canny(image):
    return cv2.Canny(image, 100, 200)

def apply_blur(image):
    return cv2.GaussianBlur(image, (11, 11), 0)

def apply_sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def apply_emboss(image):
    kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
    return cv2.filter2D(image, -1, kernel)

def plot_histogram(image):
    color = ('b', 'g', 'r')
    hist_data = {}
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        hist_data[col] = hist
    return hist_data


# Session Terminate Functions
def logout_user():
    st.session_state.logged_in = False
    st.session_state.username = ""

def is_logged_in():
    return st.session_state.get("logged_in", False)
