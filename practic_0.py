import numpy as np
import sympy as sp

alpha_deg = 45
beta_deg = 30

alpha = np.radians(alpha_deg)
beta = np.radians(beta_deg)

matrix_numeric = np.array ([[np.cos(alpha), np.sin(beta)],
                    [np.sin(alpha), np.cos(beta)]])

determinant_numeric = np.linalg.det(matrix_numeric)
print("Numerical determinant: ", determinant_numeric)

a, b = sp.symbols('a b')

matrix_symbol = sp.Matrix([[sp.cos(a), sp.sin(a)],
                    [sp.sin(b), sp.cos(b)]])

determinant_symbol = matrix_symbol.det()

print("Symbolical determinant:", determinant_symbol)

t_value = 1.0

matrix_numeric_2 = np.array([[(1 - t_value**2) / (1 + t_value**2), 2 * t_value / (1 + t_value**2)],
                             [-2 * t_value / (1 + t_value**2), (1 - t_value**2) / (1 + t_value**2)]])

determinant_numeric_2 = np.linalg.det(matrix_numeric_2)
print("Numeric determinant №2:", determinant_numeric_2)

t = sp.symbols('t')

matrix_symbolic_2 = sp.Matrix([
    [(1 - t**2) / (1 + t**2), (2 * t) / (1 + t**2)],
    [(-2 * t )/ (1 + t**2), (1 - t**2) / (1 + t**2)]
])

determinant_symbolic_2 = matrix_symbolic_2.det()
print("Symbol determinant №2:", determinant_symbolic_2)

a_value = 2.0
b_value = 3.0

matrix_numeric_3 = np.array([
    [a_value**2, a_value * b_value],
    [a_value * b_value, b_value**2]
    ])

determinant_numeric_3 = np.linalg.det(matrix_numeric_3)
print("Numeric determinant №3:", determinant_numeric_3)

a, b = sp.symbols('a b')

matrix_symbolic_3 = sp.Matrix ([
    [a**2, a*b],
    [a*a, a**2]
    ])

determinant_symbolic_3 = matrix_symbolic_3.det()
print("Symbolic determinant №3:", determinant_symbolic_3)

matrix_numeric_4 = np.array ([
    [5, 2, 0],
    [7, 3, 0],
    [0, 0, 1]
])

determinant_numeric_4 = np.linalg.det(matrix_numeric_4)
print("Numeric determinant №4:", determinant_numeric_4)

q, w, e, r, t, y, u, i, o = sp.symbols('q w e r t y u i o')

matrix_symbolic_4 = sp.Matrix ([
    [5, 2, 0],
    [7, 3, 0],
    [0, 0, 1]
])

determinant_symbolic_4 = matrix_symbolic_4.det()
print("Symbolic determinant №4:", determinant_symbolic_4)