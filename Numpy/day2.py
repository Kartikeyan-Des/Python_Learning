import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])

# root = np.sqrt(a)
# sum = np.sum(a)
# max = np.max(b)
# max = np.min(b)

# print(root)
# print(sum)
# print(max)
# print(min)

data = np.array([10, 20, 30, 40, 50])

mu = np.mean(data)

print(mu)

sub = (data - mu)

print(sub)

sqrt = sub**2

print(sqrt)