"""
    https://www.hackerrank.com/challenges/drawing-book/problem
"""
def pageCount(n, p):
    front = 0
    back = 0
    if p == 1 or p == n:
        return 0
    for x in range(1,p,2):
        front += 1
    for x in range(n, p, -2):
        if x % 2 != 0 and x -1 == p:
            break
        else:
            back += 1
    return(min(front, back))

print(pageCount(2059, 117))
