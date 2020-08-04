"""
    https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen
"""

def migratoryBirds(arr):
    types = {1:0, 2:0, 3:0, 4:0, 5:0}
    for x in arr:
        types[x] += 1
    y= max(types, key=lambda key: types[key])
    return y





n= 6
arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))