import numpy as np

x = np.array([1,2,3,4,5,6])

y = np.array([441349, 441658, 445405, 441308, 441541, 445390])

def  predict(X,theta0, theta1):
    return theta0 + theta1 * X

result = predict(7, 373859, 16179)
print(result)

def cost(X,Y,theta0,theta1):
    predictions = predict(X, theta0, theta1)
    error = Y - predictions
    return np.mean(error**2)

# print(cost(x, y, 0, 0))



def gradient_decent(X,Y,theta0,theta1,alpha,iterations):
    n = len(Y)
    for i in range (iterations):
        predictions = predict(X, theta0, theta1)
        theta0 = theta0 - alpha * (1/n) * np.sum(predictions - Y)
        theta1 = theta1 - alpha * (1/n) * np.sum((predictions - Y) * X)
    return theta0, theta1


# t0, t1 = gradient_decent(x, y, 0, 0, 0.01, 1000)
# print(t0, t1)