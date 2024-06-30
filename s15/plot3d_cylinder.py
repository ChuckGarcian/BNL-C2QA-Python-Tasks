# Title: plot3d_cylinder.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Define Domain
    radius, height = 10, 50
    theta = np.linspace(0, 2 * np.pi, 30)
    z = np.linspace(0, height, 30)
    theta, z = np.meshgrid(theta, z)

    # Compute x and y values
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plotting logic
    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")
    ax.plot_surface(x, y, z, color="red")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-height, height)
    ax.set_ylim(-height, height)
    ax.set_zlim(0, height)
    plt.show()


main()
