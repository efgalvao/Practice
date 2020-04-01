"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

    >>> num = 9669
    >>> Solution.maximum69(num)
    9969
    >>> num = 9996
    >>> Solution.maximum69(num)
    9999
    >>> num = 9999
    >>> Solution.maximum69(num)
    9999
"""


class Solution(object):
    def maximum69(num):
        """
        :type num: int
        :rtype: int
        """
        result = num
        num_l = list(map(int, str(num)))
        num_o = num_l.copy()
        l = len(num_l)
        for i in range(l):
            num_l = num_o.copy()
            num_l = list(num_l)
            if num_l[i] == 6:
                num_l[i] = 9
                num_l = [str(integer) for integer in num_l]
                num_i = int("".join(num_l))
                if num_i > result:
                    result = num_i

            else:
                num_l[i] = 6
                num_l = [str(integer) for integer in num_l]
                num_i = int("".join(num_l))
                if num_i > result:
                    result = num_i

        return result
