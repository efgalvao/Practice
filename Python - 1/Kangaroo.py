"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""
def kangaroo(x1, v1, x2, v2):
    for j in range(1, 10001):
        k1 = x1 + (v1 * j)
        k2 = x2 + (v2 * j)
        if k1 == k2:
            return 'YES'
    return 'NO'