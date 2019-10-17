class Solution:
    def combine(self, n: int, k: int):
        res = []
        self.backtrack(n, k, res, [], 1)
        return res

    def backtrack(self, n, k, res, tmp_list, ind):

        if len(tmp_list) == k:
            res.append(tmp_list[:])
            return

        tmp = tmp_list[:]
        for i in range(ind, n+1):
            tmp.append(i)
            self.backtrack(n, k, res, tmp, i + 1)
            tmp.pop()


s = Solution()

print(s.combine(4, 2))
