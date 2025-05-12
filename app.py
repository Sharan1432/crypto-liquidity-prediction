
import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load(r"C:\Users\swamy\Desktop\Crypto_Liquidity_Submission\RandomForest_Model_Save_Load.ipynb")
scaler = joblib.load(r"C:\Users\swamy\Desktop\Crypto_Liquidity_Submission\Scaler_Save_Load.ipynb")

st.title("Cryptocurrency Liquidity Prediction")

st.markdown("Enter cryptocurrency market data to predict the liquidity ratio (volume to market cap).")

# User inputs
price = st.number_input("Current Price (USD)", min_value=0.0, step=0.01)
change_1h = st.number_input("1h Price Change (%)", step=0.01)
change_24h = st.number_input("24h Price Change (%)", step=0.01)
change_7d = st.number_input("7d Price Change (%)", step=0.01)
volume_24h = st.number_input("24h Trading Volume (USD)", min_value=0.0)
market_cap = st.number_input("Market Capitalization (USD)", min_value=0.0)

# Prediction logic
if st.button("Predict Liquidity Ratio"):
    # Raw input array
    input_array = np.array([[price, change_1h, change_24h, change_7d, volume_24h, market_cap]])
    
    # Feature engineering
    volatility_24h = abs(change_24h)
    volatility_7d = abs(change_7d)
    input_array = np.append(input_array, [[volatility_24h, volatility_7d]], axis=1)
    
    # Scale input
    scaled_input = scaler.transform(input_array)
    pred = model.predict(scaled_input)
    
    st.success(f"Predicted Volume-to-MarketCap Ratio: {pred[0]:.4f}")
    st.info("Higher values indicate more liquid cryptocurrencies.")
