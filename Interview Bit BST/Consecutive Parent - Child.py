# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    count = 0

    def consecutiveNodes(self, A):

        if A.left:
            if abs(A.left.val - A.val) == 1:
                self.count += 1
            self.consecutiveNodes(A.left)
        if A.right:
            if abs(A.right.val - A.val) == 1:
                self.count += 1
            self.consecutiveNodes(A.right)

        return self.count

# another approch
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def fun(A):
    if not A:
        return 0

    ans = 0

    if A.left and abs(A.left.val - A.val) == 1:
        ans += 1
    if A.right and abs(A.right.val - A.val) == 1:
        ans += 1

    return fun(A.right) + fun(A.left) + ans


class Solution:
    # @param A : root node of tree
    # @return an integer
    def consecutiveNodes(self, A):
        return fun(A)
