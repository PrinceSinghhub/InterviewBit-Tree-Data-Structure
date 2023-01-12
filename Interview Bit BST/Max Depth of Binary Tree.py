# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, root):

        if not root:
            return 0
        Left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(Left, right) + 1
