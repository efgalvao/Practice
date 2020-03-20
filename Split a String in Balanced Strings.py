"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

>>> s = "RLRRLLRLRL"
4

>>> s = "RLLLLRRRLR"
3
>>> s = "LLLLRRRR"
1
>>> s = "RLRRRLLRLL"
2

"""
s = 'RLLLLRRRLR'
def balanced(s):
    count = 0
    strings = 0
    for n in s:
        if n == 'L':
            count += 1
            if count == 0:
                strings +=1
        elif n == 'R':
            count -= 1
            if count == 0:
                strings +=1

    return strings