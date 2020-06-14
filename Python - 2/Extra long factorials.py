"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""
def extraLongFactorials(n):
    out = 1
    for n in range(1, n+1):
        out *= n
    return out


print(extraLongFactorials(45))