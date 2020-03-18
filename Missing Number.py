"""Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        print(num_set)
        if number not in num_set:
            return number


nums = [9, 6, 4, 2, 3, 5, 7, 1, 0, 8]
print(missingNumber(nums))
