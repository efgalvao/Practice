"""
    https://www.hackerrank.com/challenges/bon-appetit/
"""
def bonAppetit(bill, k, b):
    bill.pop(k)
    total = sum(bill)
    if total / 2 == b:
        return "Bon Appetit"
    else:
        return int(b - total / 2 )


k = 1
bill = [3, 10, 2, 9]
b = 12

print(bonAppetit(bill, k, b))