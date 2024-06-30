# Title: mc_exp_dist.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from numba import float64, vectorize


@vectorize([float64(float64, float64)], nopython=True)
def exp_pdf(x: float, lambd: float):
    """
    Calculate the probability density of 'x' in an exponential distribution.
    'lambd' is the rate parameter of the exponential distribution.
    """
    return lambd * np.exp(-lambd * x) if x >= 0 else 0


@vectorize([float64(float64, float64)], nopython=True)
def exp_cum(x: float, lambd: float):
    """
    Calculate the cumulative distribution of 'x' in an exponential distribution
    'lambd' is the rate parameter of the exponential distribution.
    """

    return 1 - np.exp(-lambd * x) if x >= 0 else 0


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def main():
    # Initialize
    lambd = 1 / 90  # Rate Parameter
    t = 60
    x = np.linspace(0, 100, 1000)
    y = exp_pdf(x, lambd)

    # Generate random points
    dots = 25000
    x_random = (1 - halton(np.arange(dots), 2)) * t
    y_random = (1 - halton(np.arange(dots), 3)) * lambd * 1.5

    # Calculate Plotting Data
    d = y_random - exp_pdf(x_random, lambd)
    x_in = x_random[d <= 0.0]
    y_in = y_random[d <= 0.0]
    x_out = x_random[d > 0.0]
    y_out = y_random[d > 0.0]

    # Compute Estimate and actual
    act = exp_cum(t, lambd)
    est = np.count_nonzero(d <= 0.0) / dots
    err = np.abs((est - act) / act)

    # Show results
    print(f"dots = {dots:,}")
    print(f"act = {act:.6f}")
    print(f"est = {est:.6f}")
    print(f"err = {err:.5%}")

    # Plotting logic
    plt.figure(Path(__file__).name)
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.1)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.1)
    # fmt: off
    plt.plot(x, y, color="green", label=r"Exponential Distribution, $\lambda = 90$ minutes")
    plt.ylim(0, lambd * 1.5)
    plt.xlim(0, 70)
    plt.xlabel("Time")
    plt.ylabel("Probability Density")
    plt.tight_layout()
    plt.legend(loc="upper right", fontsize=12)
    plt.show()


main()
