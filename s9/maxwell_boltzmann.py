# Title: maxwell_boltzmann.py
# Author: Charles "Chuck" Garcia

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def maxwell_boltzmann_pdf(x, a):
    """
    Defines Maxwell-Boltzmann distribution
    """
    # Source: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution
    A = np.sqrt(2 / np.pi)
    B = pow(x, 2) / pow(a, 3)
    C = np.exp((-1 * pow(x, 2)) / (2 * pow(a, 2)))
    return A * B * C


def main():
    # Parameters
    x = np.linspace(0, 20, 1000)
    a_values = [1, 2, 5]

    # Compute plot data
    y0 = maxwell_boltzmann_pdf(x, a_values[0])
    y1 = maxwell_boltzmann_pdf(x, a_values[1])
    y2 = maxwell_boltzmann_pdf(x, a_values[2])

    # Initialize Plot figure
    plt.figure(Path(__file__).name)
    plt.title("Maxwell-Boltzmann Distribution")
    plt.xlabel("Velocity $v$ (m/s)")
    plt.ylabel("Probability Density")

    # Plot the three PDF's
    plt.plot(x, y0)
    plt.plot(x, y1)
    plt.plot(x, y2)

    # Display configuration
    plt.xlim(0, 20)
    plt.grid("on")
    plt.show()


main()
