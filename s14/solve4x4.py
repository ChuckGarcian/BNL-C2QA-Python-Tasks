# Title: solve4x4.py
# Author: Charles "Chuck" Garcia

import numpy as np

coeffs = np.array([[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]])
vals = np.array([5, 16, 22, 15])

# Create a copy of the coefficients matrix for each unknown
x1 = np.copy(coeffs)
x2 = np.copy(coeffs)
x3 = np.copy(coeffs)
x4 = np.copy(coeffs)

# Overlay the value vector on a column in each unknown's matrix
x1[:, 0] = vals
x2[:, 1] = vals
x3[:, 2] = vals
x4[:, 3] = vals


# Calculate determinant of coefficients matrix
det_coeffs = np.linalg.det(coeffs)

# Use Cramer's rule to solve 3 x 3 system of linear equations
x1 = np.linalg.det(x1) / det_coeffs
x2 = np.linalg.det(x2) / det_coeffs
x3 = np.linalg.det(x3) / det_coeffs
x4 = np.linalg.det(x4) / det_coeffs

print(rf"x1={x1:,.0f}")
print(rf"x2={x2:,.0f}")
print(rf"x3={x3:,.0f}")
print(rf"x4={x4:,.0f}")

"""
Code output:
x1=16
x2=-6
x3=-2
x4=-3
"""
