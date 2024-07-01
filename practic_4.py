import sympy as sp
import numpy as np

Tx, Ty, Tz = sp.symbols("Tx Ty Tz")
alpha, beta, gamma = sp.symbols ("alpha beta gamma")

T = sp.Matrix([
    [1, 0, 0, Tx],
    [0, 1, 0, Ty],
    [0, 0, 1, Tz],
    [0, 0, 0, 1]
])

Rz = sp.Matrix([
    [sp.cos(alpha), -sp.sin(alpha), 0, 0],
    [sp.sin(alpha), sp.cos (alpha), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

Ry = sp.Matrix([
    [sp.cos(beta), 0, sp.sin(beta), 0],
    [0, 1, 0, 1],
    [-sp.sin(beta), 0, sp.cos(beta), 0],
    [0, 0, 0, 1]
])

Rx = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.cos(gamma), -sp.sin(gamma), 0],
    [0, sp.sin(gamma), sp.cos(gamma), 0],
    [0, 0, 0, 1]
])

M = T * Rz

print("Transformation matrix M: ")
sp.pprint(M)

M_np = sp.lambdify((Tx, Ty, Tz, alpha, beta, gamma), M.evalf(), 'numpy')
print("\nTransformation matrix M (as NumPy array):")
print(M_np(10, 10, 1, sp.rad(30), sp.rad(-45), 0))
