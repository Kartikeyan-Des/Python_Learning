import numpy as np

# 1
arr1 = np.array([10,20,30,40,50])

div = arr1 / 2

print(div)

# 2

mat = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

print(mat [1:, :2])

# 3

mat = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])

col_sum = np.sum(mat, axis= 0)

print(col_sum)

# 4
mat = np.zeros((4,4))

mat = mat+10

print(mat)

# 5

vals = np.array([1, 8, 2, 10, 3, 15])

gr = vals[vals > 5]

print(gr)