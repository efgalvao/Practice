"""
https://www.hackerrank.com/challenges/encryption/
"""
import math 

def encryption(s):
    l = len(s)
    c = math.ceil(math.sqrt(l))
    f = math.floor(math.sqrt(l))
    listl =[]
    aux_i = 0
    aux_e = c
    out = []
    if f * c < l:
        f += 1
    for r in range(f):
        listl.append(s[aux_i:aux_e])
        aux_i = aux_e
        aux_e += c
    for i in range(c):
        row = []
        for j in range(f):
            teste = len(listl[j])
            if i < len(listl[j]):
                row.append(listl[j][i])
        out.append(''.join(row))
    z = ' '.join(out)
    return z  


s2 = 'feedthedog'
s = 'haveaniceday'
s3 = 'chillout'
print(encryption(s3))