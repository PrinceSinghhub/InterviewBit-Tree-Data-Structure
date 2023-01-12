# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return 0

        # checking if current node is a leaf node and then if its satisfying sum constraint
        if A.left is None and A.right is None and A.val == B:
            return 1

        return self.hasPathSum(A.left, B - A.val) or self.hasPathSum(A.right, B - A.val)

