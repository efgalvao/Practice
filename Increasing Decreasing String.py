"""
Given a string s. You should re-order the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.



>>> s = "aaaabbbbcccc"
>>> Solution.sortString(s)
'abccbaabccba'

>>> s = "rat"
>>> Solution.sortString(s)
'art'

>>> s = "leetcode"
>>> Solution.sortString(s)
'cdelotee'

>>> s = "ggggggg"
>>> Solution.sortString(s)
'ggggggg'

>>> s = "spo"
>>> Solution.sortString(s)
'ops'

"""
import string


class Solution(object):
    def sortString(s):
        """
        :type s: str
        :rtype: str
        """
        out = list()
        z = 0
        qtd = 1
        inverso = string.ascii_lowercase[::-1]
        for k in string.ascii_lowercase:
            qtdl = s.count(k)
            while qtdl > 0:
                for i in string.ascii_lowercase:
                    qtd = s.count(i) - z
                    if qtd > 0 and i in s:
                        out.append(i)
                        qtd -= 1
                z += 1
                qtdl -= 1
                for l in inverso:
                    qtd = s.count(l) - z
                    if qtd > 0 and l in s:
                        out.append(l)
                        qtd -= 1
                z += 1
                qtdl -= 1

        out = (''.join(out))
        return out

Output: "cdelotee"
s = "aaaabbbbcccc"
print(Solution.sortString(s))