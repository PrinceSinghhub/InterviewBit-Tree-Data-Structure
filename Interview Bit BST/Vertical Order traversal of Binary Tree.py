# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        if A == None:
            return []

        queue = [(A, 0)]
        ans = {}  # dict x -> [values]  for current level
        # Iterate by level, so values are properly stacked.
        while queue:
            queue2 = []
            for node, x in queue:
                ans.setdefault(x, []).append(node.val)
                if node.left is not None:
                    queue2.append((node.left, x - 1))
                if node.right is not None:
                    queue2.append((node.right, x + 1))
            queue = queue2

        return [ans[x] for x in sorted(ans.keys())]

#############################################
######### USING RECURSSION ##################

# # Definition for a  binary tree node
# # class TreeNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.left = None
# #        self.right = None

# class Solution:
#     # @param A : root node of tree
#     # @return a list of list of integers
#     def nodevert(self,root,c,d):
#         if root==None:
#             return

#         if c in self.ans:
#             self.ans[c].append([d,root.val])
#         else:
#             self.ans[c]=[[d,root.val]]

#         self.nodevert(root.left,c-1,d+1)
#         self.nodevert(root.right,c+1,d+1)


#     def verticalOrderTraversal(self, A):
#         self.ans={}

#         self.nodevert(A,0,0)

#         ans= self.ans.items()
#         ans= sorted(ans,key=lambda x: x[0])
#         for i in range(len(ans)):
#             a=ans[i][1]
#             a= sorted(a,key=lambda y:y[0])
#             for j in range(len(a)):
#                 a[j]=a[j][1]

#             ans[i]=a

#         return ans






