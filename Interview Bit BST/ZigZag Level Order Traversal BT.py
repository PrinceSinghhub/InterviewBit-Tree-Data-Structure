# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        level = [A]
        res = []
        while (level):
            nlevel = []
            l = []
            for i in level:
                l.append(i.val)
                if i.left:
                    nlevel.append(i.left)
                if i.right:
                    nlevel.append(i.right)
            level = nlevel
            res.append(l)
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res


'''class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        even_level=[root]#level 0,level 2----
        odd_level=[]#level 1,level 3,____
        level=[]
        result=[]
        while even_level or odd_level:
            while even_level:
                node=even_level.pop()
                level.append(node.val)
                if node.left:
                    odd_level.append(node.left)
                if node.right:
                    odd_level.append(node.right)
            if level!=[]:
                result.append(level)
            level=[]
            while odd_level:
                node=odd_level.pop()
                level.append(node.val)
                if node.right:
                    even_level.append(node.right)
                if node.left:
                    even_level.append(node.left)
            if level!=[]:
                result.append(level)
            level=[]
        return result'''
