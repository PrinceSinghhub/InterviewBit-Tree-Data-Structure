# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if(not A):
            return []
        q=[]
        found=False
        q.append(A)
        while(q and not found):
            s_=len(q)
            while(s_):
                p=q.pop(0)
                if((p.left and p.left.val==B) or (p.right and p.right.val==B)):
                    found=True
                else:
                    if p.left: q.append(p.left)
                    if p.right: q.append(p.right)
                s_-=1
        if not found:
            return []
        return [i.val for i in q]

