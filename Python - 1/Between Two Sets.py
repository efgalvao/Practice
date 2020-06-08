"""
https://www.hackerrank.com/challenges/between-two-sets/problem
"""
def getTotalX(a, b):
    out = []
    temp = 0
    final = 0
    for n in range(a[-1], b[0] +1):
        temp = 0
        for na in a:
            if n % na == 0:
                temp += 1                
        if temp == len(a):
            out.append(n)
    print(out)
    for z in out:
        temp = 0
        for x in b:
            if x % z == 0:
                temp += 1
        if temp == len(b):
            final += 1
    return final

a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a, b))