# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer

    def check(self, A, B):

        if A == None and B == None:
            return True

        if A == None or B == None:
            return False

        if A.val != B.val:
            return False

        l = self.check(A.left, B.left)
        r = self.check(A.right, B.right)

        return l == r

    def isSameTree(self, A, B):

        if self.check(A, B):
            return 1
        return 0