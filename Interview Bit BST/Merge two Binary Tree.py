# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        def fun(root1,root2):
            if not root2:
                return root1
            if not root1:
                return root2
            root2.val = root1.val+root2.val
            root2.left = fun(root1.left,root2.left)
            root2.right= fun(root1.right,root2.right)
            return root2
        return fun(A,B)
