# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        if not A.left and not A.right:
            if B==A.val:
                return [[B]]
            return []
        l=[]
        r=B-A.val
        # if r<=0:
        #     return l
        if A.left:
            le=self.pathSum(A.left,r)
            for i in le:
                i.insert(0,A.val)
            l.extend(le)
        if A.right:
            ri=self.pathSum(A.right,r)
            for i in ri:
                i.insert(0,A.val)
            l.extend(ri)

        return l

