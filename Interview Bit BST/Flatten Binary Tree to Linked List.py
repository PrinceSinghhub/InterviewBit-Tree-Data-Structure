# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def dfs(node):
    if node is None:
        return None
    tail = node
    left = dfs(node.left)
    right = dfs(node.right)
    if left:
        tail.right = left[0]
        tail = left[1]
    if right:
        tail.right = right[0]
        tail = right[1]
    node.left = None
    return (node, tail)


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        return dfs(A)[0]

