"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1.
"""
def square_digits(num):
    num = str(num)
    out = str()
    for n in num:
        out += str((int(n)**2))
    return int(out)

