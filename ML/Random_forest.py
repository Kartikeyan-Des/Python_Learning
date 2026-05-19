from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
Y = data.target


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, predictions))

scores = cross_val_score(model, X, Y, cv=5)

print("CV Scores: ", scores)
print("Average: ",scores.mean())