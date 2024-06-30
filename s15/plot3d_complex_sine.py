from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator


def f(x, y):
    """
    f(z) = |sin(z)|, where z is a complex number
    """
    return np.abs(np.sin(x + 1j * y))


def main():
    # Define Domain
    x = np.linspace(-2.5, 2.5, 100)
    y = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(x, y)

    # Compute the z values
    z = f(x, y)

    # Code below is from plot3d_surface.pys
    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")
    surf = ax.plot_surface(x, y, z, cmap="coolwarm", lw=0, antialiased=False)
    plt.colorbar(surf, ax=ax, shrink=0.5)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("f(z) = |sin(z)|")
    plt.show()


main()
