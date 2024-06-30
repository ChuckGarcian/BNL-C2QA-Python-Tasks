# Title: kinematics_regression.py
# Author: Charles "Chuck" Garcia

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def fit_quadratic(x, y):
    """
    Function written by David Biersach
    """
    # Reshape vector x to become matrix x
    x = x[:, np.newaxis]
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    # The matrix x2 will have two columns:
    # 1) the original x values and 2) the x**2 values
    x2 = np.array(transformer.transform(x))
    model = LinearRegression().fit(x2, y)
    a = model.coef_[1]
    b = model.coef_[0]
    c = model.intercept_
    return a, b, c


def main():
    # Extract Measured Data
    file_name = "kinematics_regression.csv"
    file_path = Path(__file__).parent / file_name
    data = np.genfromtxt(file_path, delimiter=",", skip_header=True)
    t, d = data.T

    # Compute Quadratic Regression
    a, v_i, c = fit_quadratic(t, d)
    accel = 2 * a
    print(f"Acceleration: {accel:>.05} m/s²")
    print(f"Initial Velocity: {v_i:>.05} m/s")

    # Plotting Logic
    plt.figure(Path(__file__).name)
    plt.plot(t, d, label="kinematics_regression.csv")
    plt.title("Kinematic Regression")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Distance (Meters)")
    plt.legend(fontsize=12)
    plt.show()


main()
