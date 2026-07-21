# 💰 AI Dynamic Pricing Recommendation System

An end-to-end **Machine Learning + Streamlit** project that predicts the optimal selling price for retail products using a **Random Forest Regressor**. The system analyzes demand, inventory, competitor pricing, discounts, seasonality, and other business factors to recommend an ideal product price.

---

## 📌 Project Overview

Dynamic pricing is a strategy where product prices change according to market conditions.

This project uses a **Random Forest Regression** model trained on retail inventory data to recommend the most profitable selling price.

The application provides an interactive Streamlit interface where users can enter product details and instantly receive:

- 💰 Recommended Selling Price
- 📊 Business Insights
- 📈 Prediction Summary

---

## 🚀 Features

- Interactive Streamlit Web Application
- Machine Learning Price Prediction
- Random Forest Regression Model
- Automatic Feature Engineering
- Label Encoding for Categorical Variables
- Business Recommendations
- Prediction Summary Dashboard
- Clean and User-Friendly Interface

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Machine Learning | Scikit-learn |
| Data Analysis | Pandas, NumPy |
| Visualization | Streamlit |
| Model Storage | Pickle |
| IDE | VS Code |

---

## 📂 Project Structure

```
Dynamic_Pricing_System/
│
├── app.py
├── dynamic_pricing_model.pkl
├── label_encoders.pkl
├── retail_store_inventory.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Retail Store Inventory Dataset containing:

- Store ID
- Product ID
- Category
- Region
- Inventory Level
- Units Sold
- Units Ordered
- Demand Forecast
- Discount
- Weather Condition
- Holiday/Promotion
- Competitor Pricing
- Seasonality
- Price (Target Variable)

---

## ⚙️ Feature Engineering

The following features were created before training the model:

### Date Features

- Year
- Month
- Day
- DayOfWeek

### Business Features

- Inventory Demand Ratio

```
Inventory Level / (Demand Forecast + 1)
```

- Price Difference

```
Current Price − Competitor Price
```

- Discounted Price

```
Current Price × (1 − Discount/100)
```

---

## 🤖 Machine Learning Model

Three regression algorithms were compared.

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| Linear Regression | 2.239 | 2.945 | 0.989 |
| Decision Tree | 0.830 | 1.247 | 0.998 |
| **Random Forest** ⭐ | **0.591** | **0.815** | **0.999** |

### Selected Model

✅ Random Forest Regressor

Reason:

- Highest R² Score
- Lowest MAE
- Lowest RMSE
- Best Prediction Accuracy

---

## 🖥 Application Workflow

1. Load trained Random Forest model
2. Load Label Encoders
3. User enters product details
4. Encode categorical values
5. Create engineered features
6. Generate price prediction
7. Display business recommendations
8. Show prediction summary

---

## 📸 Application Preview

### Home Screen

- Product Details Input
- Interactive Controls
- Prediction Button

### Results

- Recommended Selling Price
- Business Recommendation
- Prediction Summary

*(Add screenshots here after uploading them.)*

Example:

```
images/home.png
images/result.png
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Dynamic_Pricing_System.git
```

Move into the project folder

```bash
cd Dynamic_Pricing_System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
pickle-mixin
```

Or install directly:

```bash
pip install streamlit pandas numpy scikit-learn
```

---

## 🎯 Business Benefits

- Optimize selling prices
- Increase profitability
- Reduce inventory waste
- Improve pricing decisions
- Respond to market demand
- Stay competitive

---

## 🔮 Future Enhancements

- Real-time market pricing
- Competitor price scraping
- Demand forecasting using time series
- Power BI Dashboard Integration
- Sales Trend Visualization
- Cloud Deployment
- User Authentication
- Price History Tracking

---

## 👩‍💻 Author

**Thanuja**

Final Year B.Tech Student

Interested in:

- Data Analytics
- Machine Learning
- Artificial Intelligence
- Python Development
- Business Intelligence

GitHub: https://github.com/Thanujaroyal24

---

## ⭐ If you found this project helpful, consider giving it a Star!

```
⭐ Star this repository
🍴 Fork this repository
📢 Share it with others
```
