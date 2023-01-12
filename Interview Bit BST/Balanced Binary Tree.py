# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:

    def Findhight(self, root):

        if root == None:
            return 0
        l = self.Findhight(root.left)
        r = self.Findhight(root.right)

        if l == -1 or r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):

        if self.Findhight(A) == -1:
            return 0

        return 1
