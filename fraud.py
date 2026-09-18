# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:51:27 2026

@author: LENOVO
"""

import pandas as pd
import joblib
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


### Connect to SQL and Load Data
engine = create_engine('mysql+pymysql://root:132831@localhost/fraud_analysis')

query = "SELECT * FROM transactions"
df = pd.read_sql(query, engine)

print(df.columns.tolist())
print(df.shape)
df.head()

df.columns = df.columns.str.strip().str.lower()
print(df.columns.tolist())

X = df.drop(['isfraude','nameorig','namedest'], axis=1, errors='ignore')
y = df['isfraude']

print(X.columns.tolist())
print(y.value_counts())

X = pd.get_dummies(X, columns=['type'], drop_first=True)
X.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(X_train.shape, X_test.shape)

numerical_cols = ['step', 'amount', 'oldbalanceorg', 'oldbalancedest','newbalanceorg','newbalancedest']

scaler = StandardScaler()
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

X_train.head()
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1)

rf_model.fit(X_train, y_train)
print("Model trained successfully.")

y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

joblib.dump(rf_model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(list(X.columns), 'columns.pkl')
joblib.dump(numerical_cols, 'numerical_cols.pkl')

print("✅ Model, scaler, and columns saved successfully!")


import os
print(os.getcwd())
print(os.listdir())

