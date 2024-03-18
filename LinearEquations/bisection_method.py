import sympy as sp
import numpy as np

def max_steps(a, b, err):
    return int(np.floor(-np.log2(err / (b - a)) - 1))

def bisection_method(f, a, b, tol=1e-6, roots_list = None):
    x = sp.symbols('x')
    f_lambda = sp.lambdify(x, f)
    df = sp.diff(f)
    df_lambda = sp.lambdify(x, df)

    if np.sign(f_lambda(a)) == np.sign(f_lambda(b)):
        if np.sign(df_lambda(a)) == np.sign(df_lambda(b)):
            raise ValueError("The interval [a,b] does not bracket a root.")

    steps = max_steps(a, b, tol)
    c = 0
    for k in range(steps):
        c = (a + b) / 2
        if f_lambda(c) == 0 or (b - a) / 2 < tol:
            print(f"The equation f(x) has an approximate root at x = {c}")
            roots_list.append(c)
            return c
        if np.sign(f_lambda(a)) != np.sign(f_lambda(c)):
            b = c
        else:
            a = c

    print(f"The equation f(x) has an approximate root at x = {c}")
    roots_list.append(c)
    if abs(f_lambda(c)) > tol:
        raise ValueError("Failed to converge to a root within the specified tolerance.")
    return c

if __name__ == '__main__':
    x = sp.symbols('x')
    f = ((x**2) - (7 * x) + 6) / (2 * x**2 - 3 )
    a, b = 0, 8
    roots = []

    print('Date: 18/03/24, Group members: Raphael Benoliel 209946854, Daniel Vaknin 314753161, Maor Hadad 312469463'
          ' Bar Cohen 316164938\n Git: https://github.com/Bar1996/Numerical111/blob/main/LinearEquations/bisection_method.py,'
          ' Name: Bar Cohen ')
    print(f"Input function: {f}, Interval: [{a}, {b}]")
    jump = (b - a) / 10

    i = a + jump
    while i <= b:
        try:
            bisection_method(f, a, i, 1e-6, roots)
        except ValueError as e:
            print(f"\nNo roots found in the interval [{a}, {i}]\n")
        a = i
        i += jump

    print("All found roots:", roots)
