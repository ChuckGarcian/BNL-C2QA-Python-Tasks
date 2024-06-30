# Title: complex_factorial.py
# Author: Charles "Chuck" Garcia

from scipy.integrate import quad
import numpy as np

# Final Answer: (0.4944280270647886-0.1535275138768605j)


def f(x):
    """
    Derivation of this function:
    i! = euler_gamma (i + 1)
    < Definition of euler gamma>
    == euler_gamma (i + 1) = integral (x^i * e^(-x)
    < Given Identity x^i = e^ilnx >
    == euler_gamma (i + 1) = integral (e^ilnx * e^-x)
    < Algebra Power Rules >
    == euler_gamma (i + 1) = integral (e^ilnx -x)
    """
    if x:
        return np.exp(1j * np.log(x) - x)

    return 0


def simpsons_rule(func, a, b, intervals):
    """
    Function Author: https://github.com/dbiersach, BNL Labs
    """
    dx, area = (b - a) / intervals, func(a) + func(b)
    for i in range(1, intervals):
        area += func(a + i * dx) * (2 * (i % 2 + 1))
    return dx / 3 * area


def main():
    res = simpsons_rule(f, 0, int(1e3), int(1e5))
    print(f"i! == {res}")


main()
