'''Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None'''

class Solution:
    # @param A : root node of tree
    # @return an integer

    def isSymmetric(self, root):
        if not root:
            return 1
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return 1
        if left is None or right is None:
            return 0
        if left.val != right.val:
            return 0
        a = self.check(left.left, right.right)
        b = self.check(left.right, right.left)
        if a == b:  # a and b
            return 1
        return 0