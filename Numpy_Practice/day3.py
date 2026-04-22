import numpy as np

# # 1
# arr1 = np.array([10,20,30,40,50])

# div = arr1 / 2

# print(div)

# # 2

# mat = np.array([[1, 2, 3], 
#                 [4, 5, 6], 
#                 [7, 8, 9]])

# print(mat [1:, :2])

# # 3

# mat = np.array([[1, 2, 3], 
#                  [4, 5, 6], 
#                  [7, 8, 9]])

# col_sum = np.sum(mat, axis= 0)

# print(col_sum)

# # 4
# mat = np.zeros((4,4))

# mat = mat+10

# print(mat)

# # 5

# vals = np.array([1, 8, 2, 10, 3, 15])

# gr = vals[vals > 5]

# print(gr)

#6

sp = np.arange(12)

re = sp.reshape(3,4)

print(re)

#7

data = np.array([10, -5, 20, -1, 30, -8])

data[data < 0] = 0

loc = np.where(data == 30)

print(data)
#8
print(loc)


#9

spl = np.random.randint(1, 101, size=(4, 3))

max = np.max(spl, axis = 0)

print(max)

#10

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# add = A@B
add = np.dot(A, B)

print(add)