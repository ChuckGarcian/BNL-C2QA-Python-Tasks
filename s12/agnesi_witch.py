# Title: agnesi_witch.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sympy import Float, Number, lambdify, symbols


def calc_coeff(a, b, r, n):
    # Returns the coefficient for the nth term in the Binomial expansion of (a+b)^r
    coeff = 1.0
    for m in range(n):
        coeff = coeff * (r - m) / (m + 1)
    coeff = coeff * pow(a, r - n)
    coeff = coeff * pow(b, n)
    return coeff


def witch_power(a, b, c, r, max_t):
    """
    Power series definition of agnesi witch function.
    Credit: David Biersach from QIS github
    """
    x = symbols("x")
    poly = 0.0
    for t in range(max_t):
        poly += calc_coeff(a, b, r, t) * x ** (c * t)

    return lambdify(x, poly.as_expr(), modules="numpy")


def witch_exact(x, a):
    """
    Exact definition of agnesi witch function
    """
    return (8 * pow(a, 3)) / (pow(x, 2) + 4 * pow(a, 2))


def main():
    # Initialize Plot Figure
    plt.figure(Path(__file__).name)
    plt.title("Agnesi Witch")
    plt.xlim(-1.5, 1.5)
    plt.ylim(-2, 2)
    plt.xlabel("y")
    plt.ylabel("x")

    # Define Domain
    start = -1.5
    end = 1.5
    intervals = 1000
    x = np.linspace(start, end, intervals)

    # Compute and plot values for exact
    a = 0.5
    _witch_exact = np.vectorize(lambda _x: witch_exact(_x, a))
    y_exact = _witch_exact(x)
    plt.plot(x, y_exact, label="Exact definition")

    # Compute and plot values for aprox
    terms_start = 2
    terms_end = 8

    for t in range(terms_start, terms_end + 1):
        eqn = witch_power(1, 1, 2, -1, t)
        plt.plot(x, np.array(list(map(eqn, x))), label=f"{t} terms")

    plt.show()


main()


"""
I've considered this question for a bit, and the best explanation I 
can think of relates to the denominator of the simplified function being 
1/(x^2 + 1). In the exact analytic expression, the denominator will never be zero,
and thus f(x) will never take on undefined values. However, I think this may not 
be the case with the expansion representation. Specifically, with the expansion 
representation, as we add more terms and also as we move further away from x = 0,
there is a tendency for the expansion representation to diverge from the exact.

"""
