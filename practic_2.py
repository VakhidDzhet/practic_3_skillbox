import sympy as sp
from sympy import init_printing, pretty, latex, pprint
from sympy import Integral, symbols, Function, sqrt

x, y = sp.symbols('x y')

eq1 = sp.Eq(sp.sqrt(x - 4 * y) - 2 * sp.sqrt(x + 3 * y), 1)
eq2 = sp.Eq(7 * sp.sqrt(x + 3 * y) - 5 * x + 22 * y, 13)

solution = sp.solve((eq1, eq2), (x, y))
print("Solving a system of equations №1:")
print(solution)

import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x, y = vars
    eq1 = np.sqrt(x - 4 * y) - 2 * np.sqrt(x + 3 * y) - 1
    eq2 = 7 * np.sqrt(x + 3 * y) - 5 * x + 22 * y - 13
    return [eq1, eq2]

initial_guess = [0, 0]

solution = fsolve(equations, initial_guess)
print("Solving a system of equations №1.1:", solution)

x, y = sp.symbols('x y')

eq1 = sp.Eq((x ** 4) - (y **4), 15)
eq2 = sp.Eq((x ** 3) * y - x * (y ** 3), 6)

solution = sp.solve((eq1, eq2), (x, y))
print("Solving a system of equations №2:")
print(solution)

x, y, z = sp.symbols('x y z')

eq1 = sp.Eq(x + y + z, 2)
eq2 = sp.Eq((x ** 2) + (y ** 2) + (z ** 2), 6)
eq3 = sp.Eq((x ** 3) + (y ** 3) + (z ** 3), 8)

solution = sp.solve((eq1, eq2), (x, y))
print("Solving a system of equations №3:")
print(solution)

x, y, z = sp.symbols('x y z')

eq1 = sp.Eq((x/y) + (y/z) + (z/x), 3)
eq2 = sp.Eq((y/x) + (z/y) + (x/z), 3)
eq3 = sp.Eq(x + y + z, 3)

solution = sp.solve((eq1, eq2), (x, y))
print("Solving a system of equations №4:")
print(solution)
