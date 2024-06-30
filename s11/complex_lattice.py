# Title: complex_lattice.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Answer to part two: There are 5 gaussian integers


def fn(re, im):
    z = complex(re, im)
    return pow(z, 2) + z * 1j + 1


def fun(re, im):
    # Input into function and save outputs
    _fn = np.vectorize(fn)
    y = _fn(re, im)
    vals_x = [0] * len(y)
    vals_y = [0] * len(y)

    # Copy over the real parts and imaginary parts of f(z)
    for idx, value in enumerate(y):
        vals_x[idx] = value.real
        vals_y[idx] = value.imag

    vals_x = vals_x[::-1]
    vals_y = vals_y[::-1]

    return np.array(vals_x), np.array(vals_y)


def main():
    # Part 1 - Plot the scatter plot
    # Domain of function
    resolution = 100  # Number elements in each set
    re = np.linspace(-4, 4, resolution)  # Real part is all elements |Re(z)| <= 4
    im = np.linspace(0, 2, resolution)  # Imaginary part is all elements 0 <= Im(z) <= 2

    vals_x, vals_y = fun(re, im)

    plt.figure(Path(__file__).name)
    ax = plt.gca()
    ax.set_aspect("equal")
    ax.scatter(vals_x, vals_y)

    # Part two - Plot Gaussian integers
    re = np.arange(-10, 11)  # -10 to 10 inclusive
    im = np.arange(-10, 11)  # -10 to 10 inclusive

    vals_x, vals_y = fun(re, im)

    count = 0
    gaussian_x = []
    gaussian_y = []

    for x, y in zip(vals_x.flatten(), vals_y.flatten()):
        if abs(x) <= 10 and abs(y) <= 10:
            count += 1
            gaussian_x.append(x)
            gaussian_y.append(y)

    plt.scatter(gaussian_x, gaussian_y, color="red", s=20)
    plt.title(f"Complex Lattice (Gaussian Integers: {count})")
    plt.show()


main()
