"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""
def subtractProductAndSum(n):
    soma = sum(int(i) for i in str(n))
    multi = 1
    for num in str(n):
        multi *= int(num)

    return (multi - soma)
