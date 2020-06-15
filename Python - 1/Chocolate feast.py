'''
https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=next-challenge&h_v=zen
'''
def chocolateFeast(n, c, m):
    total = (n//c) 
    emb = total
    while emb >= m:
        emb -= m
        emb += 1
        total += 1
    return total
   
print(chocolateFeast(12951,19,5450))
print(chocolateFeast(50045,193,47247))
print(chocolateFeast(6,2,2))
