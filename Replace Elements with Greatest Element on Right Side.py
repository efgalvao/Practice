"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

"""
arr = [17, 18, 5, 4, 6, 1]


def replaceElements(arr):
    out = [-1]
    l = len(arr) - 1
    maior_direita = arr[-1]
    for i in range(l)[::-1]:
        out.append(maior_direita)
        if arr[i] > maior_direita:
            maior_direita = arr[i]


    return out[::-1]

print(replaceElements(arr))
