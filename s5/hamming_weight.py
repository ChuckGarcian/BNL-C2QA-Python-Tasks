# Title: hamming_weight.py
# Author: Charles 'Chuck' Garcia

import numpy as np

dec = 123

# Convert to binary
bin_str = np.binary_repr(dec)
bin = int(bin_str)
hamming_weight = 0

# Compute Hamming Weight 
while (bin):
  lsb = bin % 10  
  hamming_weight += lsb
  bin = bin // 10

print(f"Hamming Weight: {hamming_weight}")
