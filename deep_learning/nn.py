import numpy as np

x = np.array([
[0,0],
[0,1],
[1,0],
[1,1]
], dtype=float)

y = np.array([
[0],
[1],
[1],
[0]
], dtype=float)

np.random.seed(42)

w1 = np.random.randn(2,4) * 0.01
b1 = np.zeros((1,4))

w2 = np.random.randn(4,1) * 0.01
b2 = np.zeros((1,1))


def relu(z):
  return np.maximum(0, z)

def sigmoid(z):
  return 1/(1+ np.exp(-z))

def forward(x, w1, b1, w2, b2):
  z1 = x @ w1 + b1
  a1 = relu(z1)

  z2 = a1 @ w2 + b2
  a2 = sigmoid(z2)

  return a2, (z1, a1, z2, a2)

def loss(y, a2):
  m = y.shape[0]
  a2 = np.clip(a2, 1e-9, 1 - 1e-9)
  return -np.mean(y * np.log(a2) + (1 - y) * np.log(1 - a2))