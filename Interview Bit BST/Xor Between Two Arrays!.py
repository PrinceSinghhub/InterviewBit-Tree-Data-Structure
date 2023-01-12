class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        bigA = bigB = 0
        maxA = sorted(A)[-100:]
        maxB = sorted(B)[-100:]

        for v in A:
            for mb in maxB:
                bigA = max(bigA, v ^ mb)
        for v in B:
            for ma in maxA:
                bigB = max(bigB, v ^ ma)

        return max(bigA, bigB)