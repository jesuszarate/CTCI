'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        self.history = set()
        result = list()
        self.backtrack(result, list(), nums, 0)
        return result

    def backtrack(self, result, tmp_list, nums, k):

        current = tmp_list[:]
        if len(current) == 3 and sum(current) == 0:
            tag = "".join(sorted([str(i) for i in current]))
            if tag not in self.history:
                result.append(current)
                self.history.add(tag)
            return

        if len(tmp_list) >= 3:
            return

        for i in range(k, len(nums)):
            current.append(nums[i])
            self.backtrack(result, current, nums, i+1)
            current.pop()



s = Solution()

nums = [-1, 0, 1, 2, -1, -4]
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))