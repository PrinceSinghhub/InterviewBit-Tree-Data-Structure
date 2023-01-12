import collections
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def verticalSum(self, root):
        d=collections.defaultdict(int)
        def preorder(node,dis):
            if not node:
                return
            d[dis]+=node.val
            preorder(node.left,dis-1)
            preorder(node.right,dis+1)
        preorder(root,0)
        res=[]
        for x in sorted(d):
            res.append(d[x])
        return res
