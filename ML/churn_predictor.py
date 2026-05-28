import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv")

# print(df.shape)
# print(df.head())
# print(df.columns.tolist())

# print(df.info())
# print(df['Churn'].value_counts())
# print(df.describe())



df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print(df['TotalCharges'].isnull().sum())
df = df.dropna(subset=['TotalCharges'])
print(df.shape)
