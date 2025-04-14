import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import is_logged_in, logout_user

# Ensure the user is logged in
if not is_logged_in():
    st.warning("🚫 You must be logged in to access this page.")
    st.stop()

st.set_page_config(page_title="Car Sales Analysis", layout="wide")
st.title("🚗 Car Sales Analysis Dashboard")

# Add sidebar navigation
with st.sidebar:
    st.header("Navigation")
    if st.button("🏠 Home"):
        st.switch_page("pages/Home.py")
    if st.button("🧠 Image Analyzer"):
        st.switch_page("pages/ImageAnalyzer.py")
    if st.button("🔓 Logout"):
        logout_user()
        st.success("You have been logged out.")
        st.switch_page("pages/Home.py")

# Load the dataset
try:
    data = pd.read_csv("analysis/Car Sales.csv")  # Adjust path if needed
except FileNotFoundError:
    st.error("Car Sales dataset not found!")
    st.stop()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Data Summary
st.subheader("Data Summary")
st.write(data.describe())

# Filters
st.sidebar.header("Filter Options")
regions = data["Dealer_Region"].unique()
selected_region = st.sidebar.selectbox("Select Dealer Region", regions)

companies = data["Company"].unique()
selected_company = st.sidebar.selectbox("Select Car Company", companies)

filtered_data = data[(data["Dealer_Region"] == selected_region) & (data["Company"] == selected_company)]

# Show Filtered Data
st.subheader(f"Filtered Data for {selected_region} - {selected_company}")
st.dataframe(filtered_data)

# Visualization
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.radio("Choose Chart Type", ["Bar Chart", "Pie Chart", "Line Chart", "Histogram"])

st.subheader("Visualization")
fig, ax = plt.subplots(figsize=(8, 5))

if chart_type == "Bar Chart":
    bar_data = filtered_data["Model"].value_counts()
    ax.bar(bar_data.index, bar_data.values, color="skyblue")
    ax.set_title("Car Models Sold")
    ax.set_xlabel("Model")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
elif chart_type == "Pie Chart":
    pie_data = filtered_data["Color"].value_counts()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title("Car Color Distribution")
elif chart_type == "Line Chart":
    if "Date" in filtered_data.columns:
        filtered_data["Date"] = pd.to_datetime(filtered_data["Date"])
        sales_trend = filtered_data.groupby("Date")["Price ($)"].sum()
        ax.plot(sales_trend.index, sales_trend.values, marker="o", color="green")
        ax.set_title("Sales Trend Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Sales ($)")
        plt.xticks(rotation=45)
    else:
        st.warning("The dataset does not contain a 'Date' column for trend analysis.")
elif chart_type == "Histogram":
    ax.hist(filtered_data["Price ($)"], bins=20, color="orange", edgecolor="black")
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price ($)")
    ax.set_ylabel("Frequency")

st.pyplot(fig)

# Additional Insights
st.subheader("Additional Insights")
total_sales = filtered_data["Price ($)"].sum()
average_price = filtered_data["Price ($)"].mean()

st.success(f"💰 **Total Sales:** ${total_sales:,.2f}")
st.info(f"📉 **Average Price:** ${average_price:,.2f}")
