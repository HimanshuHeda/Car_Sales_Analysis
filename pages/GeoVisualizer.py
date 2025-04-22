import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopy.geocoders import Nominatim
from utils import is_logged_in, logout_user

st.set_page_config(page_title="GeoVisualizer", layout="wide")
st.title("🌍 GeoVisualizer - Dealer Region Plotter")

# Login check
if not is_logged_in():
    st.warning("🚫 You must be logged in to access this page.")
    st.stop()

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")
    if st.button("🏠 Home"):
        st.switch_page("pages/Home.py")
    if st.button("🔐 Login"):
        st.switch_page("pages/Login.py")
    if st.button("📝 Signup"):
        st.switch_page("pages/Signup.py")
    if st.button("🧠 Image Analyzer"):
        st.switch_page("pages/ImageAnalyzer.py")
    if st.button("📊 Car Sales Analysis"):
        st.switch_page("pages/CarSales.py")
    if st.button("🌍 GeoVisualizer"):
        st.switch_page("pages/GeoVisualizer.py")
    if st.button("🔓 Logout"):
        logout_user()
        st.success("You have been logged out.")
        st.switch_page("pages/Home.py")

# Load Car Sales data
try:
    df = pd.read_csv("analysis/Car Sales.csv")
except FileNotFoundError:
    st.error("Car Sales.csv not found!")
    st.stop()

# Extract unique Dealer_Regions
regions = df["Dealer_Region"].dropna().unique()

# Geocode each region using geopy
st.info("🔍 Geocoding Dealer Regions...")
geolocator = Nominatim(user_agent="geoapp")
geometry = []
valid_names = []

for region in regions:
    try:
        location = geolocator.geocode(region)
        if location:
            geometry.append(Point(location.longitude, location.latitude))
            valid_names.append(region)
    except Exception as e:
        st.warning(f"Skipping region '{region}': {e}")

if not geometry:
    st.error("❌ No valid regions found to plot.")
    st.stop()

# Create GeoDataFrame for points
points_gdf = gpd.GeoDataFrame({"Region": valid_names, "geometry": geometry}, crs="EPSG:4326")

# Load your custom world shapefile
try:
    world = gpd.read_file("World/ne_110m_admin_0_countries.shp")
except Exception as e:
    st.error(f"Failed to load world shapefile: {e}")
    st.stop()

# Plotting
st.subheader("🗺️ World Map with Dealer Regions")
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgrey', edgecolor='black')
points_gdf.plot(ax=ax, color='red', markersize=60)
ax.set_title("Dealer Regions on World Map", fontsize=18)

st.pyplot(fig)

# Display the data table
st.subheader("📍 Geocoded Dealer Regions")
st.dataframe(points_gdf.drop(columns="geometry"))
