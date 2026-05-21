import logging
from typing import Tuple
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

data = load_iris()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model_Pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

Pipeline.fit(x_train, y_train)
predictions = Pipeline.predict(x_test)

print(predictions)

print('Accuracy: ',accuracy_score(y_test, predictions))
scores = cross_val_score(Pipeline, x, y, cv=5)

print('Cross val Scores: ', scores)
print('Average: ',scores.mean())