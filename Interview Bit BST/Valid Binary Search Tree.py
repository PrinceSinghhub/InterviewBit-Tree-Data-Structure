# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return 0

        return 1

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

