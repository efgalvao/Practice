"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

    >>> # Testing
    >>> J = "aA"
    >>> S = "aAAbbbb"
    >>> numJewelsInStones(J, S)
    3
    >>> J = "z"
    >>> S = "ZZ"
    >>> numJewelsInStones(J, S)
    0

"""
def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    for j in J:
        for s in S:
            if j == s:
                 count +=1

    return count
