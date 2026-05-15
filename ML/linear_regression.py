import numpy as np

x = np.array([1,2,3,4,5,6])

x_train = x[:4]
x_test = x[4:]

y = np.array([441349, 441658, 445405, 441308, 441541, 445390])
y_train = y[:4]
y_test = y[4:]

def  predict(X,theta0, theta1):
    return theta0 + theta1 * X

result = predict(7, 353076, 30445)
print(result)

def cost(X,Y,theta0,theta1):
    predictions = predict(X, theta0, theta1)
    error = Y - predictions
    return np.mean(error**2)

# print(cost(x, y, 353076, 0))



def gradient_descent(X,Y,theta0,theta1,alpha,iterations):
    n = len(Y)
    for i in range (iterations):
        predictions = predict(X, theta0, theta1)
        theta0 = theta0 - alpha * (1/n) * np.sum(predictions - Y)
        theta1 = theta1 - alpha * (1/n) * np.sum((predictions - Y) * X)
    return theta0, theta1


t0, t1 = gradient_descent(x_train, y_train, 0, 0, 0.01, 1000)
print(t0, t1)

predictions = predict(x_test, t0, t1)
print("Predicted:", predictions)
print("Actual:", y_test)

MAE = np.mean(np.abs(y_test - predictions))
RMSE = np.sqrt(np.mean(y_test - predictions)**2)
R = 1 - (np.sum((y_test - predictions)**2) / np.sum((y_test - np.mean(y_test))**2))

print("MAE: ",MAE)
print("RMSE: ",RMSE)
print("R²: ",R)