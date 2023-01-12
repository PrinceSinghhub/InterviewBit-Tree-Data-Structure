class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        goods = list(set(A.split("_")))

        goodw = {}
        for g in goods:
            goodw[g] = 1
        dic = {}
        i = 0
        while (i < len(B)):
            dic[i] = 0
            for s in B[i].split("_"):
                dic[i] += goodw.get(s, 0)
            i += 1
        return [k for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)]


ans = Solution()
A = "coolicewifi"
B = ["wateriscool", "coldicedrink", "coolwifispeed"]
print(ans.solve(A,B))
