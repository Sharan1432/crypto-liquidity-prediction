# 🚀 Cryptocurrency Liquidity Prediction for Market Stability

This project uses machine learning to predict the **liquidity ratio** of cryptocurrencies based on market indicators like price, volume, market cap, and volatility.

---

## 📌 Problem Statement

Cryptocurrency markets are highly volatile. A lack of liquidity can cause instability and sharp price movements. This project aims to:
- Predict the **volume-to-market-cap ratio** (a liquidity proxy)
- Detect early signs of low liquidity
- Help traders and platforms manage risk effectively

---

## 📁 Dataset

- Source: [CoinGecko Historical Data](https://www.coingecko.com/)
- Dates Used: `2022-03-16` and `2022-03-17`
- Features: `price`, `1h/24h/7d % changes`, `24h volume`, `market cap`

---

## 🛠 Project Pipeline

```
Raw CSV Data
     ↓
Data Cleaning & Normalization
     ↓
Feature Engineering (Volatility, Liquidity Ratios)
     ↓
Model Training (Random Forest)
     ↓
Evaluation (R², MAE, MSE)
     ↓
Streamlit Deployment
```

---

## 📊 Key Features

- 📈 **EDA Visuals**: Volume leaders, correlation heatmap
- 🔍 **Feature Engineering**: Volume-to-market-cap ratio, volatility
- 🌲 **Model**: Random Forest Regressor
- 🎯 **Metrics**: R² ≈ 0.59, MAE ≈ 0.036
- 🌐 **Deployment**: Streamlit app for liquidity prediction

---

## 🧪 Evaluation

| Metric   | Value     |
|----------|-----------|
| R² Score | ~0.59     |
| MAE      | ~0.036    |
| MSE      | ~0.006    |

---

## 🧾 Project Structure

```
.
├── source_code.ipynb           # Full end-to-end ML notebook
├── app.py                      # Streamlit app script
├── rf_model.pkl                # Trained model file
├── scaler.pkl                  # Fitted scaler
├── EDA_Report.pdf              # EDA summary and plots
├── Pipeline_Architecture.pdf   # ML pipeline flow diagram
├── HLD_LLD_Document.docx       # Design docs
├── Final_Report.docx           # Project summary report
├── Presentation.pptx           # Slides for presentation
```

---

## 🖥️ Run Locally

```bash
# Install dependencies
pip install streamlit joblib pandas scikit-learn

# Run the Streamlit app
streamlit run app.py
```

---

## 📄 License

This project is part of an academic/portfolio submission. Please credit the author if reused.
