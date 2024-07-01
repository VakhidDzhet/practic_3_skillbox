import numpy as np

B = np.array([
    [1.2],
    [3.3],
    [5.1]
])

C = np.array([
    [3.2],
    [4.5],
    [0.3]
])

A = np.array([
    [0.1, 2.1, 4.1],
    [3.2, 1.8, 2.6],
    [1.1, 6.2, 3.4]
])

C_B = C - B

A_inv = np.linalg.inv(A)

X = np.dot(A_inv, C_B)

print("Matrix X:")
print(X)

B = np.array([
    [9, 5, 2],
    [4, 7, 6],
    [4, 7, 2]
])

C = np.array([
    [5, 3, 7],
    [8, 9, 9],
    [3, 1, 7]
])

A = np.array([
    [8, 9, 2],
    [8, 2, 5],
    [1, 9, 6]
])

C_B = C - B

A_inv = np.linalg.inv(A)

X = np.dot(A_inv, C_B)

print("Matrix X №2:")
print(X)