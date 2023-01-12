# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):

        arr = []

        if root == None:
            return []

        if root.left != None:
            arr += self.postorderTraversal(root.left)

        if root.right != None:
            arr += self.postorderTraversal(root.right)

        if root != None:
            arr.append(root.val)
        return arr


# another Approch
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):

        arr = []

        if root == None:
            return []

        # if root.left!=None:
        arr += self.postorderTraversal(root.left)

        # if root.right!=None:

        arr += self.postorderTraversal(root.right)

        if root != None:
            arr.append(root.val)
        return arr


