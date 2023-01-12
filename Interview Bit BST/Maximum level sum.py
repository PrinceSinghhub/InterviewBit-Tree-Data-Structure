# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

from collections import deque
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        res = float("-inf")
        q = deque([A])

        while q:
            curSum = 0
            for i in range(len(q)):
                node = q.popleft()

                curSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res = max(res, curSum)

        return res
