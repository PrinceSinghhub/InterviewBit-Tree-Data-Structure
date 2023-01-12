# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        path1 = self.getPath(A, B)
        path2 = self.getPath(A, C)
        lca = -1
        for a, b in zip(path1, path2):
            if a is not b:
                break
            lca = a.val

        return lca

    def getPath(self, root, val):
        if not root:
            return []
        if root.val == val:
            return [root]

        left = self.getPath(root.left, val)
        right = self.getPath(root.right, val)
        if right:
            return [root] + right
        if left:
            return [root] + left
        return []

