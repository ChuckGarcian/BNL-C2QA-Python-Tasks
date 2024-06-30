# Title: euelers_constant.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
from scipy.integrate import quad

import numpy as np
import matplotlib.pyplot as plt


def eulers_constant(x):
    """
    Returns an approximation of euler's constant when integrated
    """
    return -1 * np.log(np.log(1 / x))


def harmonic_number(n):
    """
    Returns the nth harmonic number
    """
    nat_numbers = np.arange(1, n + 1)
    return np.sum(1 / nat_numbers)


def main():
    # Eulers Constant
    a, b = 0, 1
    eulers_constant_aprox = quad(eulers_constant, a, b, full_output=True)[0]
    print(f"Aproximiation of Eulers Constant: {eulers_constant_aprox}")

    # First 50 harmonic numbers
    start = 1
    end = 50
    n = np.arange(start, end + 1)
    _harmonic_number = np.vectorize(harmonic_number)
    harmonic_data = _harmonic_number(n)

    # Eulers + ln (x) Data
    y = eulers_constant_aprox + np.log(n)

    # Plotting Logic
    plt.figure(Path(__file__).name)
    plt.title("Harmonic Numbers")
    plt.xlabel("N'th Value")
    plt.ylabel("Harmonic Number")
    plt.step(n, harmonic_data)
    plt.plot(n, y)
    plt.show()


main()
