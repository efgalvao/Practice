"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

>>> nums = [2, 7, 11, 15]
>>> target = 9
[0, 1]
>>> nums = [3, 3]
>>> target = 6
[0, 1]

"""

def twoSum(nums, target):
    for i in nums:
        ij = 0
        for j in nums:
            print(ij)
            if i + j == target and nums.index(i) != ij:
                return [nums.index(i), ij]
            ij += 1

nums = [3, 3]
target = 6
print(twoSum(nums, target))
