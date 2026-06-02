import numpy as np
import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import joblib

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
df = df.drop('customerID', axis=1)
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0 })
df = pd.get_dummies(df, drop_first=True)
print(df.shape)


y = df['Churn']
x = df.drop('Churn', axis=1)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100,class_weight='balanced', random_state=42)
model.fit(x_train, y_train)

joblib.dump(model, 'churn_model.pk1')
print("Model saved")

predictions = model.predict(x_test)
print("Accuracy: ", accuracy_score(y_test, predictions))

print(classification_report(y_test, predictions))


scores = cross_val_score(model, x, y, cv=5)

print("Cv score: ", scores)
print("Average: ", scores.mean())