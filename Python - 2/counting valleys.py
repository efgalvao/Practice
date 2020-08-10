"""
    https://www.hackerrank.com/challenges/counting-valleys/problem
"""
def countingValleys(n, s):
    valleys = 0
    aux = 0
    stri = [x for x in s]
    for s in stri:
        print(s)
        if s == "D":
            aux -= 1
        else:
            aux += 1
        if aux == -1:
            valleys += 1
    return valleys

n = 8
s = "UDDDUDUU"
print(countingValleys(n, s))