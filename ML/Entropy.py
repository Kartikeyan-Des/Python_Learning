import numpy as np

# X = np.array([1,1,1,1])
# Y = np.array([1,0,1,0])

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) 

y_left = Y[:4]
y_right = Y[4:]



def entropy(Z):
    values, count = np.unique(Z, return_counts=True)
    n = len(Z)
    probability = count/n
    entropy = -np.sum(probability * np.log2(probability))
    return entropy

# result = entropy(y_right)
# print(result)


def Weight_Average(y_left, y_right,Y):
    yl = len(y_left)
    yr = len(y_right)
    y = len(Y)
    entropyl = entropy(y_left)
    entropyr = entropy(y_right)
    weight = (yl/y) * entropyl + (yr/y) * entropyr
    return weight

def information_gain(E, AE):
    return E - AE

weighted = Weight_Average(y_left, y_right, Y)
ig = information_gain(entropy(Y), weighted)

print("Information gained: ", ig)