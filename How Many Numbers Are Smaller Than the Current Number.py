"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
def smallerNumbersThanCurrent(nums):
    resultado = []
    a = 0
    for i in nums:
        resultado.append(0)
        for j in nums:
            if j < i:
                resultado[a] = resultado[a] + 1

        a += 1

    return resultado
