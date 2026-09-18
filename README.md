# FRAUD-DETECTION
Develop an end-to-end machine learning pipeline that extracts transaction data from a SQL database, analyzes and engineers features, trains multiple classifiers, and deploys the strongest model as an interactive fraud-screening tool.
🕵️ Fraud Detection App

A machine learning web app that predicts whether a financial transaction is likely fraudulent, built on the PaySim-style mobile money transaction dataset and deployed with Streamlit.

## 🔍 Overview

This project trains and compares three classifiers (Logistic Regression, Random Forest, XGBoost) to detect fraudulent transactions, then deploys the best-performing model — **Random Forest** — as an interactive web app.

- **11,142** transactions analyzed
- **10.25%** fraud rate in the dataset
- **0.97 recall / 1.00 precision** on the fraud class (final model)

## ⚙️ How It Works

1. Transaction data is pulled from a MySQL database and cleaned in Python (pandas, SQLAlchemy)
2. Features are preprocessed: one-hot encoding for transaction type, StandardScaler for numeric columns
3. Three models are trained and evaluated; Random Forest is selected for its balance of accuracy and simplicity
4. The trained model is saved (`model.pkl`, `scaler.pkl`, `columns.pkl`) and loaded into a Streamlit app for real-time predictions

## 🧠 Model Details

| Metric | Score (Fraud class) |
|---|---|
| Precision | 1.00 |
| Recall | 0.97 |
| F1-score | 0.98 |
| Overall Accuracy | 1.00 |

**Features used:** `step`, `type`, `amount`, `oldbalanceOrg`, `oldbalanceDest`
*(Only pre-transaction data is used — no information that wouldn't be available in real time.)*

## 🚀 Live App

👉 [Add your Streamlit Cloud link here once deployed]

## 🛠️ Tech Stack

- **Python** (pandas, scikit-learn, joblib)
- **MySQL** + SQLAlchemy (data source, training only)
- **Streamlit** (web app / deployment)

-
  <img width="958" height="760" alt="image" src="https://github.com/user-attachments/assets/de4eb960-ecc6-47fe-989e-f77004cb9944" />

  <img width="1063" height="606" alt="image" src="https://github.com/user-attachments/assets/68ed7d2f-abf1-49d1-af33-3375f6cb17ec" />

