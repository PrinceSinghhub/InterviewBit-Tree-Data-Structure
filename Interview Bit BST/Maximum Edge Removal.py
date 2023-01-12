class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        if A<=3:
            return 0
        p = [0 for i in range(A+1)]
        e = [0 for i in range(A+1)]
        p[1] = -1
        for i in range(len(B)):
            p[B[i][1]] = B[i][0]
            e[B[i][0]]+=1
        for i in range(A,1,-1):
            e[p[i]]+=e[i]
        ans = 0
        for i in range(2,A+1):
            if e[i]%2:
                ans+=1
        return ans


