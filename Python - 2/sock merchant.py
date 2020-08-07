"""
    https://www.hackerrank.com/challenges/sock-merchant/problem
"""
def sockMerchant(n, ar):
    pairs = 0
    socks = {}
    for s in ar:
        socks[f"{s}"] = socks.get(f"{s}", 0) + 1
    for v in socks.values():
        pairs += v // 2
    return pairs

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))