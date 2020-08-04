"""
    https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if i < j and (ar[i] + ar[j]) % k == 0 :
                count += 1
    return count

n = 6 
k = 3
ar = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(n, k, ar))
