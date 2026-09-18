# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 00:50:06 2026

@author: LENOVO
"""

import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and column structure
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columns.pkl')
numerical_cols = joblib.load('numerical_cols.pkl')

st.title("🕵️ Fraud Detection App")
st.write("Enter transaction details below to check if it's likely fraudulent.")

# --- Input fields ---
step = st.number_input("Step", min_value=0, value=1)
transaction_type = st.selectbox("Transaction Type", ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceorg = st.number_input("Old Balance (Origin)", min_value=0.0, value=1000.0)
oldbalancedest = st.number_input("Old Balance (Destination)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_dict = {
        'step': step,
        'amount': amount,
        'oldbalanceorg': oldbalanceorg,
        'oldbalancedest': oldbalancedest,}
    

    # One-hot columns (drop_first=True dropped CASH_IN as the base category)
    for t in ['CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']:
        input_dict[f'type_{t}'] = 1 if transaction_type == t else 0

    input_df = pd.DataFrame([input_dict])

    # Match training column order exactly
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Scale numerical columns
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Result")
    if prediction == 1:
        st.error(f"⚠️ Likely FRAUD (Probability: {probability:.2%})")
    else:
        st.success(f"✅ Not Fraud (Probability of fraud: {probability:.2%})")