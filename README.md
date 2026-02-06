# House Price Prediction System

An end-to-end Machine Learning project that predicts residential housing prices in Ames, Iowa based on 79 explanatory variables. This project demonstrates the full ML lifecycle: from data cleaning and EDA to model building and deployment via a Streamlit web app.

## Live Demo
*(Optional: If you deploy this later, put the link here. For now, you can leave this blank or add a GIF of your app running locally)*

## Project Overview
Real estate pricing is complex and often relies on intuition. This project aims to bring data-driven precision to valuation using regression techniques.

* **Problem:** Predict the final sale price of a home.
* **Goal:** Minimize the Root Mean Squared Error (RMSE) between predicted and actual prices.
* **Dataset:** [Kaggle Ames Housing Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) (1460 training samples, 81 features).

## Tech Stack
* **Language:** Python 3.10+
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Model Persistence:** Joblib
* **Web App:** Streamlit
* **IDE:** VS Code

## Project Structure
```text
HousePricePrediction/
├── data/                # Raw training and test data (not on git)
├── models/              # Saved model artifacts (.pkl files)
├── notebooks/           # Jupyter notebooks for EDA and experimentation
├── src/                 # Source code for scripts (if needed)
├── app.py               # Streamlit frontend application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation