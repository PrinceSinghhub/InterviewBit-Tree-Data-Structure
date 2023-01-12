from collections import deque


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        S = []
        Q = deque()
        Q.append(root)

        # Do something like normal level order traversal order.
        # Following are the differences with normal level order
        # traversal:
        # 1) Instead of printing a node, we push the node to stack
        # 2) Right subtree is visited before left subtree
        while (len(Q) > 0):

            # Dequeue node and make it root
            root = Q.popleft()
            S.append(root)

            # Enqueue right child 
            if (root.right):
                Q.append(root.right)

                # Enqueue left child
            if (root.left):
                Q.append(root.left)

                # Now pop all items from stack one by one and print them
        ans = []
        while (len(S) > 0):
            root = S.pop()
            ans.append(root.val)
        return ans