"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac = 0
    oc = 0
    for ap in apples:
        if (ap + a) >= s and (ap + a) <= t:
            ac +=1
    for o in oranges:
        if (o + b) >= s and (o + b) <= t:
            oc +=1
    return ac, oc

