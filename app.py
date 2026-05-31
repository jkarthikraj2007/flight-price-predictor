import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib

if not os.path.exists("model.pkl"):
    import train

# Page config
st.set_page_config(page_title="Flight Price Predictor", page_icon="✈️", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .stApp {background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);}
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&display=swap');

    .hero-title {
        text-align: center;
        color: white;
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 0.3rem;
        font-family: 'Montserrat', sans-serif;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }
    .hero-subtitle {
        text-align: center;
        color: #cbd5e0;
        font-size: 1.5rem;
        margin-bottom: 2.5rem;
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        -webkit-font-smoothing: antialiased;
    }
    .section-header {
        color: #90cdf4;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 1.8rem;
        margin-bottom: 0.8rem;
        border-left: 3px solid #667eea;
        padding-left: 10px;
    }
    .price-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    }
    .price-label {
        color: rgba(255,255,255,0.75);
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }
    .price-amount {
        color: white;
        font-size: 3.5rem;
        font-weight: 900;
        line-height: 1;
    }
    .price-meta {
        color: rgba(255,255,255,0.65);
        font-size: 0.9rem;
        margin-top: 0.8rem;
    }
    .tip-box {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin-top: 1.5rem;
        color: #a0aec0;
        font-size: 0.88rem;
    }
    .stSelectbox label, .stSlider label {
        color: #e2e8f0 !important;
        font-weight: 500;
        font-size: 0.9rem;
    }
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    div[data-baseweb="select"] * {color: white !important;}
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.85rem;
        border-radius: 12px;
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 1.5rem;
        letter-spacing: 0.5px;
        transition: opacity 0.2s;
    }
    .stButton > button:hover {opacity: 0.85;}
    .divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.08);
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# Hero
st.markdown('<p class="hero-title">✈️ Flight Price Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Predict Indian domestic flight prices instantly using Machine Learning</p>', unsafe_allow_html=True)

# Route Details
st.markdown('<p class="section-header">🛫 Route Details</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    source_city = st.selectbox("Source City", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"])
with col2:
    destination_city = st.selectbox("Destination City", ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Chennai"])

# Flight Details
st.markdown('<p class="section-header">🏷️ Flight Details</p>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    airline = st.selectbox("Airline", ["SpiceJet", "AirAsia", "Vistara", "GO_FIRST", "Indigo", "Air_India"])
with col4:
    travel_class = st.selectbox("Class", ["Economy", "Business"])

col5, col6 = st.columns(2)
with col5:
    departure_time = st.selectbox("Departure Time", ["Morning", "Early_Morning", "Afternoon", "Evening", "Night", "Late_Night"])
with col6:
    arrival_time = st.selectbox("Arrival Time", ["Morning", "Early_Morning", "Afternoon", "Evening", "Night", "Late_Night"])

col7, col8 = st.columns(2)
with col7:
    stops = st.selectbox("Number of Stops", ["zero", "one", "two_or_more"])
with col8:
    duration = st.slider("Duration (hours)", 1.0, 50.0, 2.0)

# Booking Details
st.markdown('<p class="section-header">📅 Booking Details</p>', unsafe_allow_html=True)
days_left = st.slider("Days Left to Departure", 1, 49, 10)

# Predict
if st.button("Predict Price ✈️"):

    def make_prediction(days):
        input_data = pd.DataFrame(columns=columns)
        input_data.loc[0] = 0
        input_data["duration"] = duration
        input_data["days_left"] = days
        input_data[f"airline_{airline}"] = 1
        input_data[f"source_city_{source_city}"] = 1
        input_data[f"destination_city_{destination_city}"] = 1
        input_data[f"departure_time_{departure_time}"] = 1
        input_data[f"arrival_time_{arrival_time}"] = 1
        input_data[f"stops_{stops}"] = 1
        input_data[f"class_{travel_class}"] = 1
        return model.predict(input_data)[0]

    # Current price
    price = make_prediction(days_left)

    # Price card
    st.markdown(f"""
        <div class="price-card">
            <p class="price-label">Estimated Flight Price</p>
            <p class="price-amount">₹{price:,.0f}</p>
            <p class="price-meta">{airline} &nbsp;·&nbsp; {source_city} → {destination_city} &nbsp;·&nbsp; {travel_class} &nbsp;·&nbsp; {stops} stop(s)</p>
        </div>
    """, unsafe_allow_html=True)

    # Tip
    if days_left < 7:
        tip = "⚠️ Booking very close to departure — prices are likely at their peak!"
    elif days_left < 15:
        tip = "💡 Prices are rising. Consider booking soon for a better deal."
    else:
        tip = "✅ Good time to book! Prices tend to be lower when booked in advance."

    st.markdown(f'<div class="tip-box">{tip}</div>', unsafe_allow_html=True)

    # Price trend chart
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">📈 Price Trend — Days Left vs Price</p>', unsafe_allow_html=True)
    st.caption("See how the price changes depending on when you book")

    day_range = list(range(1, 50))
    prices = [make_prediction(d) for d in day_range]

    chart_df = pd.DataFrame({
        "Days Left to Departure": day_range,
        "Predicted Price (₹)": prices
    })

    st.line_chart(chart_df.set_index("Days Left to Departure"))

    # Best day to book
    best_day = day_range[np.argmin(prices)]
    best_price = min(prices)
    st.markdown(f"""
        <div class="tip-box">
            🏆 <b>Best time to book:</b> {best_day} days before departure &nbsp;·&nbsp; Estimated price: <b>₹{best_price:,.0f}</b>
        </div>
    """, unsafe_allow_html=True)