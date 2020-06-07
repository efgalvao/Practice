"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
"""
def persistence(n):
    n = [int(i) for i in str(n)]
    counter = 0
    while (len(n) > 1) :
        t = 1
        for i in n:
            t *= i
        n = [int(i) for i in str(t)]
        counter += 1
    return counter

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))