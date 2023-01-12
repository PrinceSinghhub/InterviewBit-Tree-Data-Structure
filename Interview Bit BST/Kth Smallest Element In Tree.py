# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer

    def inOrderTraversal(self, root):

        if root == None:
            return []

        left = self.inOrderTraversal(root.left)
        right = self.inOrderTraversal(root.right)

        return left + [root.val] + right

    def kthsmallest(self, root, B):
        arr = self.inOrderTraversal(root)

        arr.sort()
        return arr[B - 1]


