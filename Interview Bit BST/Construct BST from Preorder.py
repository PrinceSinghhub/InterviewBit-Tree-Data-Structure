import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def constructBST(self, arr):
        n=len(arr)
        root=TreeNode(arr[0])
        stack=[root]
        for i in range(1,n):
            node=TreeNode(arr[i])
            if arr[i]<stack[-1].val:
                stack[-1].left=node
                stack.append(node)
            else:
                while stack and stack[-1].val<arr[i]:
                    x=stack.pop()
                x.right=node
                stack.append(node)
        return root
