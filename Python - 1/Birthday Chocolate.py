"""
https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""
def birthday(s, d, m):
    len_s = len(s)
    out = 0
    for n in range(len_s):
        count = 0
        aux = n
        while aux < m +n and m + n <= len_s:
            count += s[aux]
            aux += 1
        if count == d:
            out +=1
    return out

s = [1, 2, 1, 3, 2]
d = 3 
m = 2       
s2 = [4]
d2 = 4
m2 = 1
#print(birthday(s, d, m)) 
print(birthday(s2, d2, m2)) 

