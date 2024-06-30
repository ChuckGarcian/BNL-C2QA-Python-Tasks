# Title: custom_cf.py
# Author: Charles "Chuck" Garcia

import numpy as np
import math

MAX_TERMS = 7


# Credit: Foundations of Quantum Information Science (QIS102)
def normalize_cf(cf):
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf


# Credit: Foundations of Quantum Information Science (QIS102)
def encode_cf(x):
    cf: list[int] = []
    while len(cf) < MAX_TERMS:
        cf.append(int(x))
        x = x - int(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


# Credit: Foundations of Quantum Information Science (QIS102)
def decode_cf(cf):
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in cf:
        a_n, b_n = term, 1
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
    return h_n / k_n


# Credit: Foundations of Quantum Information Science (QIS102)
def eval_cf(x):
    cf = encode_cf(x)
    x2 = decode_cf(cf)
    print(f"{x} -> {cf} -> {x2}")


def main():
    print("Listing CF's from 1 to 9:")
    for n in range(1, 10):
        x = (1 + math.sqrt(4 * pow(n, 2) - 4 * n + 5)) / 2
        eval_cf(x)
    print("Done")


main()
