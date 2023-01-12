# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:

    def inOrder(self, root):

        if root == None:
            return []

        ans = []

        ans += self.inOrder(root.left)
        if root != None:
            ans.append(root.val)
        ans += self.inOrder(root.right)

        return ans

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):

        arr = self.inOrder(A)

        i, j = 0, len(arr) - 1

        while (i != j):
            if (arr[i] + arr[j] == B):
                return 1
            elif (arr[i] + arr[j] > B):
                j = j - 1
            else:
                i = i + 1
        return 0


