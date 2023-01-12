# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def getLeftHeight(self, A):
        c = 0
        while A:
            c += 1
            A = A.left
        return c

    def lastNode(self, A):
        h = self.getLeftHeight(A)

        if h == 1:
            return A.val

        if h - 1 == self.getLeftHeight(A.right):
            return self.lastNode(A.right)

        return self.lastNode(A.left)

