def plusMinus(arr):
    l = len(arr)
    p = 0
    n = 0
    z = 0
    for n in arr:
        if n > 0:
            p += 1
        elif n < 0:
            n += 1
        else:
            z += 1
    print(float(p/l))
    print(float(n/l))
    print(float(z/l))

print(plusMinus([-4, 3, -9, 0, 4, 1]))