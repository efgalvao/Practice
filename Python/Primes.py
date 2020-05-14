"""
Count the number of prime numbers less than a non-negative number, n.

>>> n = 10
>>> countPrimes(n)
4
"""

def primos(n):
    primos = 1
    for i in range(3, n):
        divisores = 2
        if i % 2 == 0:
            continue
        for j in range(2, i//2 + 1):
            if i % j == 0:
                divisores += 1
                break
        if divisores == 2:
            primos += 1
    return primos

print(primos(10000))
