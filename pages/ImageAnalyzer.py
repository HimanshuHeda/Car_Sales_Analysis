import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from utils import *
from utils import is_logged_in, logout_user

# Check login status
if not is_logged_in():
    st.warning("🚫 You must be logged in to access this page.")
    st.stop()

st.set_page_config(page_title="Image Analyzer", layout="wide")
st.title("🧠 AI-Powered Image Analyzer & Visualizer")

# Add sidebar navigation
with st.sidebar:
    st.header("Navigation")
    if st.button("🏠 Home"):
        st.switch_page("pages/Home.py")
    if st.button("🚗 Car Sales Analysis"):
        st.switch_page("pages/CarSales.py")
    if st.button("🔓 Logout"):
        logout_user()
        st.success("You have been logged out.")
        st.switch_page("pages/Home.py")

# Sidebar
st.header("Upload Image")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    st.sidebar.header("Processing Options")
    option = st.sidebar.selectbox("Choose a filter", [
        "Original", "Grayscale", "Canny Edges", "Blur", "Sharpen", "Emboss"
    ])

    if option == "Original":
        result = image_bgr
    elif option == "Grayscale":
        result = convert_to_grayscale(image_bgr)
    elif option == "Canny Edges":
        result = apply_canny(image_bgr)
    elif option == "Blur":
        result = apply_blur(image_bgr)
    elif option == "Sharpen":
        result = apply_sharpen(image_bgr)
    elif option == "Emboss":
        result = apply_emboss(image_bgr)

    # Display Result
    st.subheader("🖼 Processed Image")
    if len(result.shape) == 2:
        st.image(result, channels="GRAY", use_container_width=True)
    else:
        result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        st.image(result_rgb, use_container_width=True)

    # Show Histogram
    if len(result.shape) == 3:
        st.subheader("📊 Color Histogram")
        hist = plot_histogram(image_bgr)
        fig, ax = plt.subplots()
        for col, data in hist.items():
            ax.plot(data, color=col)
        ax.set_xlim([0, 256])
        st.pyplot(fig)

