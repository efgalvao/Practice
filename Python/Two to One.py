"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters,

    each taken only once - coming from s1 or s2.
"""
def longest(s1, s2):
    longe = list(set(s1).union(set(s2)))
    longe = sorted(longe)
    longe ="".join(longe)
    return longe

print(longest("aretheyhere", "yestheyarehere")) #"aehrsty"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding")) #"abcdefghilnoprstu")
print(longest("inmanylanguages", "theresapairoffunctions")) #"acefghilmnoprstuy")