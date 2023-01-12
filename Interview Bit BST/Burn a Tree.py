# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import collections


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        def path(root, val):
            stack = []
            stack.append((root, 0))
            while len(stack) > 0:
                node, state = stack.pop()
                if state == 2 or (node.left is None and node.right is None):
                    if node.val == val:
                        stack.append((node, None))
                        return [node for node, _ in stack]
                else:
                    if state == 0:
                        stack.append((node, 1))
                        if node.left:
                            stack.append((node.left, 0))
                    else:
                        stack.append((node, 2))
                        if node.right:
                            stack.append((node.right, 0))

        def reroot(root, val):
            stack = path(root, val)
            right = True
            for i in range(len(stack) - 1, 0, -1):
                if right:
                    stack[i].right = stack[i - 1]
                else:
                    stack[i].left = stack[i - 1]
                right = True if stack[i - 1].right == stack[i] else False
                if right:
                    stack[i - 1].right = None
                else:
                    stack[i - 1].left = None
            return stack[-1]

        def maxdepth(root):
            queue = collections.deque()
            queue.append(None)
            queue.append(root)
            level = 0
            while len(queue):
                node = queue.popleft()
                if node is None:
                    if len(queue):
                        level += 1
                        queue.append(None)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return level - 1

        root = reroot(A, B)

        return maxdepth(root)

