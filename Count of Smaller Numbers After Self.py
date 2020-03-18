"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""
# Proposition #1
def countSmaller(nums):
    counts = []
    r = 0
    a = 1
    for i in nums:
        a = len(counts)
        counts.append(0)
        while a < len(nums):
            if i > nums[a]:
                counts[r] += 1
                a += 1
            else:
                a += 1

        r += 1


    return counts

# Proposition #2
def countSmaller1(nums):
    counts = []
    for i in range(len(nums)):
        menores = 0
        for s in range(i + 1, len(nums)):
            if nums[i] > nums[s]:
                menores += 1

        counts.append(menores)

    return counts
nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(countSmaller1(nums))

# Proposition #3
def countSmaller2(nums):
    ret = []
    for i in range(len(nums)):
        smaller = 0
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                smaller += 1
        ret.append(smaller)

    return ret
print(countSmaller2(nums))

nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]

#[4, 3, 2, 1, 4]
print(countSmaller(nums))
