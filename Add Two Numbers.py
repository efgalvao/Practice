"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

>>> l1[2, 4, 3]
>>> l2[5, 6, 4]
>>> addTwoNumbers(l1, l2)
[7, 0, 8]

"""

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    num1 = []
    while l1 != None:
        num1.append(l1.val)
        l1 = l1.next

    num1 = num1[::-1]
    num1 = int(''.join(str(i) for i in num1))

    num2 = []
    while l2 != None:
        num2.append(l2.val)
        l2 = l2.next

    num2 = num2[::-1]
    num2 = int(''.join(str(i) for i in num2))

    soma = (str(num1 + num2))[::-1]

    lista = ListNode(int(soma[0]))
    out = lista

    for i in range(1, len(soma)):
        node = ListNode(int(soma[i]))
        out.next = node
        out = out.next

    return lista
