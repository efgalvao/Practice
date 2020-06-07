"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

>>> S = "(()())(())"
>>> removeOuterParentheses(S)
'()()()'

>>> S = "(()())(())(()(()))"
>>> removeOuterParentheses(S)
'()()()()(())'

>>> S = "()()"
>>> removeOuterParentheses(S)
''

"""
def removeOuterParentheses(S: str) -> str:
    left = 0
    right = 0
    sl = list(S)
    for i in range((len(S)-1), 0, -1):
        if S[i] == '(':
            left += 1
            if left == 2 and S[i] == last:
                sl.pop(i)
                left -= 2

        else:
            right += 1
            if right == 2 and S[i] == last:
                sl.pop(i)
                right -= 2

        last = S[i]
    return ''.join(sl)

ent = "(()())(())(()(()))"
Output: "()()()()(())"
print(removeOuterParentheses(ent))
