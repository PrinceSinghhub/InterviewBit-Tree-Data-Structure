# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
		if not B:
			return None
		root_pos = B.index(A[0])
		new_node = TreeNode(A[0])
		new_node.left = self.buildTree(A[1:root_pos+1], B[:root_pos])
		new_node.right = self.buildTree(A[root_pos+1:], B[root_pos+1:])
		return new_node

