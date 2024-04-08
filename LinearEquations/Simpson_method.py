import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')
def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

    return integral


if __name__ == '__main__':
    f = lambda x: (6*x**2 - math.cos(x**4 - x + 2)) / (x**2 + x + 2)
    n = 146

    a=3.0
    b=4.1

    print('Date: 08/04/24, Group members: Raphael Benoliel 209946854, Daniel Vaknin 314753161, Maor Hadad 312469463'
          ' Bar Cohen 316164938\n Git: https://github.com/Bar1996/Numerical111/blob/main/LinearEquations/Simpson_method.py,'
          ' Name: Bar Cohen ')
    print("f = lambda x: math.e ** (x ** 2)")
    print(f"n = {n}")
    print(f"a = {a}")
    print(f"b = {b}")

    print( f" Division into n={n} sections ")
    integral = simpsons_rule(f, a, b, n)
    print(f"Numerical Integration of definite integral in range [{a},{b}] is {integral}")