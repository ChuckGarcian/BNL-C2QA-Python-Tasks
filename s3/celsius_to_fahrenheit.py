# Title: celsius_to_fahrenheit.py
# Author: Charles "Chuck" Garcia

import numpy as np

def main():
    # Range and step
    start = -44
    stop = 104
    step = 4

    # Conversion logic
    cels_vec = np.arange(start, stop, step)
    fahr_vec = (cels_vec * 1.8) + 32
    
    # Pretty Print
    for cels, fahr in zip(cels_vec, fahr_vec):
        print(f"C: {cels:2.2f} → F: {fahr:2.2f}")


main()
