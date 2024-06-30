# Title: random_walk_gamma.py
# Author: Charles "Chuck" Garcia

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def E_dist(x, N):
    '''
    Defines given function 
    '''
    num = sp.gamma((x + 1) / 2)
    denom = sp.gamma(x / 2)
    return np.sqrt((2 * N) / x) * (num / denom) ** 2


def main():
    # Bounds
    N = 20_000
    d = (1, 25)

    # Generate Plotting Data 
    E_dist_np = np.vectorize(E_dist)
    x = np.arange(d[0], d[1] + 1, 1)
    y = E_dist_np(x, N)

    # Plot Logic
    plt.figure(Path(__file__).name)
    plt.plot(x, y)
    plt.grid("on")
    plt.show()


main()
