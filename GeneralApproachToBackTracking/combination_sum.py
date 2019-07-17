class Solution:
    def combinationSum(self, candidates, target):
        self.result = []

        candidates.sort()
        self.rec(candidates, [], target, 0)
        return self.result


    def rec(self, candidates, lst, target, ind):
        current_list = lst.copy()
        if target == 0:
            self.result.append(current_list)
            return

        if target < 0:
            return

        for i in range(ind, len(candidates)):
            current_list.append(candidates[i])
            self.rec(candidates, current_list, target - candidates[i], i)
            del current_list[-1]

s = Solution()

print(s.combinationSum([2, 3, 6, 7], 7))

