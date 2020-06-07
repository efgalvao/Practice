"""
 A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""

def selfDividingNumbers(left: int, right: int):
    out = []
    for i in range(left, right + 1):
        if i < 10:
            out.append(i)
        else:
            temp = str(i)
            count = 0
            for d in temp:
                if int(d) == 0:
                    break
                elif i % int(d) != 0:
                    break
                elif i % int(d) == 0:
                    count += 1
            if count == len(temp):
                out.append(i)

    return out

print(selfDividingNumbers(1,10000))