def canRepresentBST(pre):
    s = []

    root = -2 ** 32

    for value in pre:
        if value < root:
            return 0
        while (len(s) > 0 and s[-1] < value):
            root = s.pop()
        s.append(value)
    return 1


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        s = {}
        for x in A:
            if x in s:
                return 0
            s[x] = 1
        return canRepresentBST(A)
