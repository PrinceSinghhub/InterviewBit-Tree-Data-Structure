# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        root = A
        succ = root

        while root.val != B:
            if B < root.val:
                succ = root
                root = root.left
            else:
                root = root.right

        if root.right != None:
            root = root.right
            while root.left != None:
                root = root.left
            return root
        else:
            if succ.val <= B:
                return None
            else:
                return succ



