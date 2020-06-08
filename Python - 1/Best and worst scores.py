"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""
def breakingRecords(scores):
    best = 0
    best_score = scores[0]
    worst = 0
    worst_score = scores[0]
    for g in scores:
        if g > best_score:
            best += 1
            best_score = g
        elif g < worst_score:
            worst += 1
            worst_score = g
    return best, worst

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores))