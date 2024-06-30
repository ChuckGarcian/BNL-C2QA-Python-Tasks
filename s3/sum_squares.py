# Title: sum_squares.py
# Author: Charles "Chuck" Garcia

import numpy as np


def main():
    # Initialize 
    n = 1000
    vec = np.arange(1, n + 1)

    # Compute Actual and expected values
    sum_result = np.sum(vec**2)
    expected = (2 * (n**3) + 3 * (n**2) + n) / 6

    # Show results
    print(f"Expected: {expected:,.0f}")
    print(f"Actual:   {sum_result:,.0f}")


main()
