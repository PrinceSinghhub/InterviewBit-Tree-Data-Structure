# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):

        ans = []

        if A == None:
            return []

        if A != None:
            ans.append(A.val)

        ans += self.preorderTraversal(A.left)

        ans += self.preorderTraversal(A.right)

        return ans
