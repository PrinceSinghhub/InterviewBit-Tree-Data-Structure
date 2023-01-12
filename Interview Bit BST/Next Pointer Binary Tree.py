# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        dummy = tail = TreeLinkNode(0)
        while root and root.left:
            tail.next = root.left
            tail = tail.next
            tail.next = root.right
            tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next

