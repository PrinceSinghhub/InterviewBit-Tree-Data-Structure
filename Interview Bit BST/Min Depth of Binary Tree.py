# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, root):

        if root == None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0:
            return left + right + 1

        return min(left, right) + 1
