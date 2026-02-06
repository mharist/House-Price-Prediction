# House Price Prediction System

An end-to-end Machine Learning project that predicts residential housing prices in Ames, Iowa. This project demonstrates the full ML lifecycle: from data cleaning and EDA to training an advanced XGBoost model (91% accuracy) and deploying it via a Streamlit web app.

## Key Results
| Model | R² Score | Performance |
| :--- | :--- | :--- |
| **Linear Regression** (Baseline) | 0.65 | Captures basic trends but misses complex patterns. |
| **XGBoost Regressor** (Final) | **0.91** | **Significant improvement.** Captures non-linear relationships and interactions. |

## Tech Stack
* **Language:** Python 3.10+
* **ML Libraries:** Scikit-Learn, XGBoost, Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **App Framework:** Streamlit
* **Version Control:** Git & GitHub

## Project Structure
```text
HousePricePrediction/
├── data/                # Raw training and test data
├── models/              # Saved model artifacts (XGBoost .pkl)
├── notebooks/           # Jupyter notebooks for EDA and experimentation
├── src/                 # Source code
├── app.py               # Streamlit frontend application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation