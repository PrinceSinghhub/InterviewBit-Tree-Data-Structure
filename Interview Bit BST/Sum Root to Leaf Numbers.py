# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):

        ans = 0

        def dfs(node, till=0):
            nonlocal ans
            if not node: return
            if node.left == None and node.right == None:
                ans = (ans + till * 10 + node.val) % 1003
                return
            dfs(node.left, (till * 10) + node.val)
            dfs(node.right, (till * 10) + node.val)

        dfs(A)

        return ans
