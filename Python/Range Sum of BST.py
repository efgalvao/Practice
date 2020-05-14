"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def rangeSumBST(root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        s = 0
        valor = int(root.val)
        print(type(valor))
        while valor > L:
            left = int(root.left.val)
            right = int(root.right.val)
            if left > L:
                s = s + left
            if right > L:
                s = s + right
            root.val = root.left
            valor = int(root.val)
            print(type(valor), s)

        t = []
        s = 0


root = TreeNode(10,5,15,3,7,null,18)
L = 7
R = 15
print(rangeSumBST(root, 7, 15))
"""       while t:
            t.add(str(t))
            t.next

        for i in t:
            if i >= L or i <= R:
                s += i

        return s
"""
