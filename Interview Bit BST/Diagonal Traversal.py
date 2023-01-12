# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorder(self, node, d, l):
        if not node:
            return
        d[l].append(node.val)
        self.preorder(node.left, d, l+1)
        self.preorder(node.right, d, l)
    def solve(self, A):
        from collections import defaultdict
        d = defaultdict(list)
        self.preorder(A, d, 0)

        ans = []
        for k in sorted(d.keys()):
            for i in d[k]:
                ans.append(i)
        return ans  