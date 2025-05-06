# 🚗 Car Sales Analyzer & GeoVisualizer

**AI-Powered Car Sales Analysis Dashboard** built using **Streamlit**, **Python**, and various data and image processing libraries. This project provides a secure, interactive platform to analyze car sales data, apply real-time image filters, and visualize dealer regions on a world map.

---

## 🔍 Features

* 📊 **Car Sales Dashboard**

  * Filter sales by `Dealer Region`, `Company`, and `Model`
  * Visualize data using bar and pie charts
  * See total and average sales in real time

* 🧠 **Image Analyzer**

  * Upload and process images with filters
  * Grayscale, Canny Edges, Blur, Sharpen, Emboss
  * Histogram visualization (RGB channels)

* 🌍 **GeoVisualizer (Future Scope)**

  * Visualize `Dealer_Region` data on a custom world map
  * Powered by `GeoPandas` and `geopy`
  * Uses shapefiles to map geographic points (in progress)

* 🔐 **Authentication System**

  * Secure `Sign Up` and `Login`
  * Passwords hashed using `SHA-256`
  * Session-based access to protect dashboard routes

---

## 🧰 Tech Stack & Libraries

* **Frontend/UI**: Streamlit
* **Backend/Data**: Python, Pandas, JSON
* **Data Visualization**: Matplotlib, GeoPandas
* **Image Processing**: OpenCV (`cv2`), NumPy, PIL
* **Security**: hashlib (SHA-256), Streamlit `session_state`
* **Geo Mapping**: GeoPandas, geopy, custom shapefiles

---

## 📂 Folder Structure

```
Car_Sales_Analysis/
├── Home.py                      # Landing page with background image
├── utils.py                    # Utility functions for login, image filters, etc.
├── users.json                  # Stores user credentials (hashed)
├── analysis/
│   └── Car Sales.csv           # Sales dataset
├── World/
│   └── ne_110m_admin_0_countries.shp  # World shapefile
├── assets/
│   └── car_bg.jpg              # Background image
├── pages/
│   ├── Login.py
│   ├── Signup.py
│   ├── CarSales.py
│   ├── ImageAnalyzer.py
│   └── GeoVisualizer.py
```

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/HimanshuHeda/Car_Sales_Analysis.git
cd Car_Sales_Analysis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run Home.py
```

---

## 📈 Dataset Used

* File: `Car Sales.csv`
* Fields: `Dealer_Region`, `Company`, `Model`, `Color`, `Price ($)`

---

## 👥 Contributors

* **Himanshu Heda**

---

## 🌟 Future Enhancements

* Complete integration of GeoMapping via GeoPandas
* Add persistent database (SQLite/PostgreSQL)
* Export charts and dashboards as PDF/Excel
* Add user-specific dashboards and profile management

---

## 📎 License

This project is open-source and free to use under the MIT License.

---

## 🔗 GitHub

[Visit Project Repository](https://github.com/HimanshuHeda/Car_Sales_Analysis)
