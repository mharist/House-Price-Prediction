import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Load the model AND the column names
# We need both to make predictions
model = joblib.load('models/xgb_model.pkl')
model_columns = joblib.load('models/model_columns.pkl')

# 2. Define the UI
st.title("🏡 House Price Prediction App (XGBoost)")
st.write("Enter the details of the house to estimate its price.")

# 3. User Inputs (We'll pick the top 3 most important features for now)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=500, max_value=5000, value=1500)
overall_qual = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
year_built = st.number_input("Year Built", min_value=1800, max_value=2024, value=2000)

# 4. Prediction Button
if st.button("Predict Price"):
    
    # Create a dataframe with all columns initialized to zeros
    # This aligns our input with exactly what the model expects
    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = 0  # Fill with zeros initially
    
    # Fill in the user inputs
    if 'GrLivArea' in input_data.columns:
        input_data['GrLivArea'] = gr_liv_area
    if 'OverallQual' in input_data.columns:
        input_data['OverallQual'] = overall_qual
    if 'YearBuilt' in input_data.columns:
        input_data['YearBuilt'] = year_built

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    st.success(f"Estimated Price: ${prediction:,.2f}")

    # Debugging: Show the user what data was sent to the model
    with st.expander("See input data sent to model"):
        st.write(input_data)