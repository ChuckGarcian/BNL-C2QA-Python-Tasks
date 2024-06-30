# Title: sum_squares.py
# Author: Charles "Chuck" Garcia

import numpy as np

def main():
    # Initialize vector
    n = 1900
    vec = np.arange(1, n + 1)

    # Compute Sum
    sum_result = 0
    for i in vec:
        if (not (i % 7 or i % 11)):
          sum_result += i        
    
    # Show results
    print (sum_result)

main()
