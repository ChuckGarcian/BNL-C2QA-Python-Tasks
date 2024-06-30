# Title: benfords_law.py
# Author: Charles 'Chuck' Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mpf, power, log, floor, fdiv


def raise_and_msd(n):
    """
    Given integer 'n', raises n to 100'th power and returns it's msd
    """
    # Convert given number into an mpf number since its largeeee!
    m = mpf(str(n))

    # Satisfy 100'th power requirement
    m = power(m, 100)

    # -- Now we want to compute the MSD --
    # Compute Place Value
    msd_pow = floor(log(m, 10))
    place_value = power(10, msd_pow)

    # Dividing the integer 'm' by the place value should extract the MSD for us
    MSD = fdiv(m, place_value)
    MSD = floor(MSD)  # Since we only care about the integer part of MSD

    return int(MSD)


def count(values):
    """
    Returns an array of size 10 with the counts populated in
    """
    res = [0] * 10

    for i in values:
        res[i] += 1

    return res


def main():
    # Parameters
    low = 1
    high = 1_000_000
    size = 100_000

    # vectorize makes it so that the passed function works on numpy objects
    _raise_and_msd = np.vectorize(raise_and_msd)
    data = np.random.randint(low, high, size)
    plotting_data = _raise_and_msd(data)
    plotting_data = count(plotting_data)

    # Plot Logic
    plt.figure(Path(__file__).name)
    plt.bar(np.arange(10), plotting_data)
    plt.title(f"Benfords Law ({size:,})")
    plt.xticks(np.arange(10))
    plt.xlabel("Integer MSD's")
    plt.ylabel("Counts")
    plt.show()


main()
