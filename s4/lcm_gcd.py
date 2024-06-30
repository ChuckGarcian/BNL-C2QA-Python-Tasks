# Title: lcm_gcd.py
# Author: Charles "Chuck" Garcia

import numpy as np


def lcm(a, b):
    """
    Returns the lcm of integers 'a' and 'b'
    """
    return (a * b) / np.gcd(a, b)


def main():
    # Task - display 447618, and 2011835
    a = 447618
    b = 2011835
    print(f"The lcm of {a:>,} and {b:>,} is {lcm(a,b):>,.0f}")

    # Run Simple test suite
    rng = np.random.default_rng()
    a_rand = rng.integers(low=0, high=100, size=1000)
    b_rand = rng.integers(low=0, high=100, size=1000)

    for a, b in zip(a_rand, b_rand):
        assert lcm(a, b) == np.lcm(a, b)


main()
