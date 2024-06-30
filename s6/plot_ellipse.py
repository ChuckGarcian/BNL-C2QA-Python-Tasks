# plot_ellipse.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Two degrees of freedom
    a = 100
    b = 50

    # Compute Radi
    theta = np.linspace(0, 2 * np.pi, 1000)
    num = (a**2) * (b**2)
    denom = (b**2) * (np.cos(theta) ** 2) + (a**2) * (np.sin(theta) ** 2)
    radius = np.sqrt(num / denom)

    # Convert to Cartesian
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plotting logic
    plt.figure(Path(__file__).name)
    plt.title("Ellipse!")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, y)
    plt.grid("on")
    plt.show()


main()
