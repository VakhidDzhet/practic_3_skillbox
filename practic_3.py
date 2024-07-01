#Решение первого ОДУ
import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

ode = sp.Eq(y.diff(x) + x * y**2, 5 * x * y)

solution = sp.dsolve(ode, y, ics={y.subs(x, 0): 1})

sp.pprint(solution)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, x):
    dydx = 5 * x * y - x * y**2
    return dydx

y0 = 1

x = np.linspace(0, 5, 100)

sol = odeint(model, y0, x)

plt.plot(x, sol, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Numerical Solution of ODE')
plt.grid(True)
plt.show()

import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

ode = sp.Eq(y.diff(x) + 3 * sp.cos(x) ** 2, y * (x))

solution = sp.dsolve(ode, y, ics={y.subs(x, 0): 0})

sp.pprint(solution)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, x):
    dydx = y - 3 * np.cos(x) ** 2
    return dydx

y0 = 0

x = np.linspace(0, 5, 100)

sol = odeint(model, y0, x)

plt.plot(x, sol, label='Numerical Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Numerical Solution of ODE')
plt.grid(True)
plt.show()

