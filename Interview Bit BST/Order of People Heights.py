class Solution:
    # @param H : list of integers
    # @param I : list of integers
    # @return a list of integers
    def order(self, H, I):
        N = len(H)
        data = {H[i]: I[i] for i in range(N)}
        print(data)

        positions = list(range(N))

        res = [None] * N

        for k in sorted(data.keys()):
            res[positions[data[k]]] = k
            del positions[data[k]]

        return res

ans = Solution()
Heights = [5,3,2,6,1,4]
InFronts = [0,1,2,0,3,2]
print(ans.order(Heights,InFronts))