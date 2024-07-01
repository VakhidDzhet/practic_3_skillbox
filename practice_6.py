import numpy as np
from scipy.linalg import expm, sinm, cosm

a11 = 1
a12 = 2
a21 = 3
a22 = 4

A = np.array([[a11, a12], [a21, a22]])

exp_A = expm(A)

sin_A = sinm(A)

cos_A = cosm(A)

print("exp(A):")
print(exp_A)
print("\nsin(A):")
print(sin_A)
print("\ncos(A):")
print(cos_A)

A = np.array([
    [5, 7, 4],
    [1, 2, 1],
    [3, 1 ,4]
])

exp_A = expm(A)

sin_A = sinm(A)

cos_A = cosm(A)

print("exp(A) №2:")
print(exp_A)
print("\nsin(A) №2:")
print(sin_A)
print("\ncos(A) №2:")
print(cos_A)