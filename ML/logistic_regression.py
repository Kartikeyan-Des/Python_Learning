import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


def sigmoid(z):
    return 1/(1 + np.exp(-z))


def predict(X, theta0, theta1):
    z = theta0 + theta1 * X
    return sigmoid(z)


# result = predict(X, 0, 0)
# print(result)

def Gradient_descent(X, Y, theta0, theta1, alpha, iterations):
    n= len(Y)
    for i in range(iterations):
        predictions = predict(X, theta0, theta1)
        theta0 = theta0 - alpha * (1/n) * np.sum(predictions - Y)
        theta1 = theta1 - alpha * (1/n) * np.sum((predictions - Y) * X)
    return theta0, theta1

t0, t1 = Gradient_descent(X,Y,0,0,0.01,1000)

print(t0)
print(t1)


predictions = predict(X, t0, t1)
print("probabilities", predictions)

classified = (predictions >= 0.5).astype(int)
print("Classified", classified)
print("Actual", Y)


TP = np.sum((classified==1) & (Y == 1))
TN = np.sum((classified == 0) & (Y == 0))
FP = np.sum((classified == 1) & (Y == 0))
FN = np.sum((classified == 0) & (Y == 1))

Accuracy = (TP + TN) / len(Y)
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)

f1 = 2* (Precision * Recall) / (Precision + Recall)

print("Accuracy",Accuracy)
print("Precision",Precision)
print("Recall",Recall)
print("f1",f1)