import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Dynamic Pricing Recommendation System",
    page_icon="💰",
    layout="wide"
)

# -------------------------------
# LOAD MODEL
# -------------------------------
with open("dynamic_pricing_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Label Encoders
with open("label_encoders.pkl", "rb") as file:
    label_encoders = pickle.load(file)

# -------------------------------
# LOAD DATASET
# -------------------------------
df = pd.read_csv("retail_store_inventory.csv")

# -------------------------------
# TITLE
# -------------------------------
st.title("💰 AI Dynamic Pricing Recommendation System")
st.markdown(
"""
This application recommends an optimal selling price using a
Random Forest Machine Learning model trained on retail inventory data.
"""
)

st.divider()

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("About")

st.sidebar.success(
"""
**Model Used**

✅ Random Forest Regressor

**Dataset**

Retail Store Inventory Dataset

**Purpose**

Recommend the best selling price based on demand,
inventory and competitor pricing.
"""
)

# -------------------------------
# USER INPUTS
# -------------------------------

st.header("Enter Product Details")

col1, col2 = st.columns(2)

with col1:

    store = st.selectbox(
        "Store ID",
        sorted(df["Store ID"].unique())
    )

    product = st.selectbox(
        "Product ID",
        sorted(df["Product ID"].unique())
    )

    category = st.selectbox(
        "Category",
        sorted(df["Category"].unique())
    )

    region = st.selectbox(
        "Region",
        sorted(df["Region"].unique())
    )

    inventory = st.number_input(
        "Inventory Level",
        min_value=0,
        value=150
    )

    units_sold = st.number_input(
        "Units Sold",
        min_value=0,
        value=100
    )

    units_ordered = st.number_input(
        "Units Ordered",
        min_value=0,
        value=100
    )

with col2:

    demand = st.number_input(
        "Demand Forecast",
        min_value=0.0,
        value=120.0
    )

    discount = st.slider(
        "Discount (%)",
        0,
        20,
        5
    )

    weather = st.selectbox(
        "Weather Condition",
        sorted(df["Weather Condition"].unique())
    )

    holiday = st.selectbox(
        "Holiday / Promotion",
        [0,1]
    )

    competitor = st.number_input(
        "Competitor Pricing",
        min_value=0.0,
        value=50.0
    )
    current_price = st.number_input(
    "Current Price",
    min_value=0.0,
    value=50.0
)

    season = st.selectbox(
        "Seasonality",
        sorted(df["Seasonality"].unique())
    )
    

st.divider()

predict_button = st.button(
    "🚀 Recommend Price",
    use_container_width=True
)
price_difference = current_price - competitor
discounted_price = current_price * (1 - discount / 100)
# =====================================================
# PREDICTION
# =====================================================

if predict_button:

    # ----------------------------
    # Encode categorical values
    # ----------------------------

    store_encoded = label_encoders["Store ID"].transform([store])[0]
    product_encoded = label_encoders["Product ID"].transform([product])[0]
    category_encoded = label_encoders["Category"].transform([category])[0]
    region_encoded = label_encoders["Region"].transform([region])[0]
    weather_encoded = label_encoders["Weather Condition"].transform([weather])[0]
    season_encoded = label_encoders["Seasonality"].transform([season])[0]

    # ----------------------------
    # Today's Date Features
    # ----------------------------

    today = datetime.today()

    year = today.year
    month = today.month
    day = today.day
    dayofweek = today.weekday()

    # ----------------------------
    # Inventory Demand Ratio
    # ----------------------------

    inventory_ratio = inventory / (demand + 1)

    # ----------------------------
    # Create Feature DataFrame
    # ----------------------------

    input_df = pd.DataFrame({

    "Store ID":[store_encoded],
    "Product ID":[product_encoded],
    "Category":[category_encoded],
    "Region":[region_encoded],
    "Inventory Level":[inventory],
    "Units Sold":[units_sold],
    "Units Ordered":[units_ordered],
    "Demand Forecast":[demand],
    "Discount":[discount],
    "Weather Condition":[weather_encoded],
    "Holiday/Promotion":[holiday],
    "Competitor Pricing":[competitor],
    "Seasonality":[season_encoded],
    "Year":[year],
    "Month":[month],
    "Day":[day],
    "DayOfWeek":[dayofweek],
    "Inventory_Demand_Ratio":[inventory_ratio],
    "Price_Difference":[price_difference],
    "Discounted_Price":[discounted_price]

})
    input_df = input_df[model.feature_names_in_]

    st.write("Input Columns:")
    st.write(input_df.columns.tolist())

    st.write("Model Columns:")
    st.write(list(model.feature_names_in_))

    st.write("DataFrame:")
    st.dataframe(input_df)

    prediction = model.predict(input_df)[0]

    prediction = round(prediction,2)

    st.metric(
    label="💰 Recommended Selling Price",
    value=f"₹ {prediction}")


    st.divider()

    st.subheader("📈 Business Recommendation")

    if demand > 150:
        st.write("✅ High demand detected. A higher selling price is recommended.")

    elif demand < 60:
        st.write("⚠️ Demand is low. Consider promotional pricing.")

    if inventory < 100:
        st.write("📦 Inventory is running low. Increasing price may maximize profit.")

    elif inventory > 350:
        st.write("📦 High inventory available. Lower pricing may improve sales.")

    if competitor > prediction:
        st.write("🏪 Competitor price is higher than your recommended price.")

    else:
        st.write("🏪 Competitor price is lower. Be careful with overpricing.")

    if holiday == 1:
        st.write("🎉 Holiday or Promotion detected. Customer demand may increase.")

    if discount >= 15:
        st.write("🏷️ Large discount selected. Monitor profit margins.")
    difference = prediction - current_price

    if difference > 0:
        st.success(f"Increase price by ₹{difference:.2f}")
    else:
        st.warning(f"Reduce price by ₹{abs(difference):.2f}")
    st.divider()

    st.subheader("📊 Prediction Summary")

    summary = pd.DataFrame({

        "Feature":[
            "Demand Forecast",
            "Inventory Level",
            "Competitor Price",
            "Discount",
            "Recommended Price"
        ],

        "Value":[
            demand,
            inventory,
            competitor,
            discount,
            prediction
        ]

    })

    st.dataframe(summary, use_container_width=True)
    