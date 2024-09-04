# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10-4 are acceptable.
# Example: arr = [1,1,0,-1,-1]
# There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5=0.400000, 2/5=0.400000, and 1/5=0.200000. 
# Results are printed as:
# 0.400000
# 0.400000
# 0.200000

import math
import os
import random
import re
import sys

def plusMinus(arr):
    
    n = len(arr)
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)

    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)