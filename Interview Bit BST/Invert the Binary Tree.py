# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):

        if A != None:
            temp = A.left
            A.left = self.invertTree(A.right)
            A.right = self.invertTree(temp)
            return A
