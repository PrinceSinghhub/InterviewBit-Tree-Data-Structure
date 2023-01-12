# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def helper(node, arr, target):
    if not node:
        return False
    arr.append(node.val)
    if node.val == target:
        return True
    if helper(node.left, arr, target) or helper(node.right, arr,target):  # if any of the side satisfying or finf target return True
        return True
    arr.pop()  # if left and right no returned true remove that node in that specific recursion level
    return False


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        arr = []
        if A == None:
            return A
        helper(A, arr, B)
        return arr
