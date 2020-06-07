"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix

is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal =
. The right to left diagonal = . Their absolute difference is

.

Function description

Complete the

function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

    arr: an array of integers .

Input Format

The first line contains a single integer,
, the number of rows and columns in the matrix .
Each of the next lines describes a row, , and consists of space-separated integers

.

Constraints

Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15

Explanation

The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
"""
def diagonalDifference(arr):
    times = len(arr[0])
    x = 0
    suml = 0
    sumr = 0
    while x < times:
        suml += arr[x][x]
        x += 1
    x = times - 1
    y = 0
    while x >= 0:
        sumr += arr[x][y]
        x -= 1
        y += 1
    out = abs(suml - sumr)
    return out

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))