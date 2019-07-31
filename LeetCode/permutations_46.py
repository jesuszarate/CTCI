'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        results = []
        self.backtrack(results, list(), nums)
        return results

    def backtrack(self, result, tmp_list, nums):

        if len(tmp_list) == len(nums):
            result.append([i for i in tmp_list])
            return

        for i in range(len(nums)):
            if nums[i] not in tmp_list:
                tmp_list.append(nums[i])
                self.backtrack(result, tmp_list, nums)
                tmp_list.pop()





s = Solution()

print(s.permute([1,2,3]))