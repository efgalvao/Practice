"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.


    >>> print(getDecimalValue([1,0,1]))
    5


    >>> head = [0]
    >>> print(getDecimalValue(head))
    0


    >>> head = [1]
    >>> print(getDecimalValue(head))
    1


    >>> head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    >>> print(getDecimalValue(head))
    18880


    >>> head = [0,0]
    >>> print(getDecimalValue(head))
    0

"""

def getDecimalValue(head):
    """
    :type head: ListNode
    :rtype: int
    """
    nums = ''
    for i in head:
        nums += str(i)

    dec = int(nums, 2)
    return dec
