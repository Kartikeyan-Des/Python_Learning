import numpy as np

x = np.array([1,2,3,4,5,6])

y = np.array([441349, 441658, 445405, 441308, 441541, 445390])

def  predict(X,theta0, theta1):
    return theta0 + theta1 * X

result = predict(x, 0, 0)
print(result)

