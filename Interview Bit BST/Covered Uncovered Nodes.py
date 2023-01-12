# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

from queue import Queue
class Solution:
    # @param A : root node of tree
    # @return an integer
    def coveredNodes(self, A):
        cover = 0
        uncover = 0
        q = Queue()
        q.put(A)
        level = 0
        while (q.empty()==False):
            n = q.qsize()
            for i in range(n):
                node = q.get()
                if (i == 0 or i == n - 1):
                    uncover += node.val
                else:
                    cover += node.val
                if (node.left != None):
                    q.put(node.left)
                if (node.right != None):
                    q.put(node.right)
        return abs(cover - uncover)
