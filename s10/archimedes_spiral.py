# Title: archimedes_spiral.py
# Author: Charles "Chuck" Garcia

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def func_arch(theta):
    """
    Helper function to compute the arc distance of an archimedes spiral
    """
    # Derive functions for x and y
    x_prime = 1 * np.cos(theta) + theta * -1 * np.sin(theta)
    y_prime = 1 * np.sin(theta) + theta * np.cos(theta)

    # Source: https://i.ytimg.com/vi/UhuxxkOocdY/maxresdefault.jpg
    return np.sqrt(pow(x_prime, 2) + pow(y_prime, 2))


def main():
    # Compute Polar data
    a, b = 0, 8 * np.pi
    steps = 1000
    theta = np.linspace(a, b, steps, endpoint=True)
    r = theta

    # Convert Polar to Euclidean
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Take Integral to get final arc distance
    arc_length = quad(func_arch, a, b, full_output=True)[0]
    print(f"Arc Length of archimedes spiral: {arc_length}")

    # Plotting Logic
    plt.figure(Path().name)
    plt.title("Archimedes Spiral")
    plt.xlabel("r")
    plt.ylabel("theta")
    plt.plot(x, y)
    plt.grid("on")
    plt.show()


main()
