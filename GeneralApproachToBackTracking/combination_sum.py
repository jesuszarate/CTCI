

'''
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
'''
class CombinationSum:

    def combination(self, nums, target):

        lst = list()

        self.backtrack(lst, list(), nums, target, 0)

        return lst

    def backtrack(self, lst, tmp_lst, nums, target, ind):

        if target == 0:
            lst.append([i for i in tmp_lst])
            return

        for i in range(ind, len(nums)):

            if target - nums[i] >= 0:
                tmp_lst.append(nums[i])
                self.backtrack(lst, tmp_lst, nums, target - nums[i], i)
                del tmp_lst[-1]


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(CombinationSum().combination(candidates, target))
