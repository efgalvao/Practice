"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

    >>> nums = [12,345,2,6,7896]
    >>> findNumbers(nums)
    2
    >>> nums = [555,901,482,1771]
    >>> findNumbers(nums)
    1

"""
def findNumbers(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            count += 1

    return count

