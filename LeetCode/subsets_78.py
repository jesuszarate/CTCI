'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
]
'''



class Solution:
    '''
    *** Usually use and index that we pass down when we want unique items. ***
    '''
    def subsets(self, nums):
        results = list()
        nums.sort()
        self.backtrack(results, list(), nums, 0)
        return results

    def backtrack(self, results, tmp_list, nums, ind):
        results.append([i for i in tmp_list]) # Make a copy of the temp and add it to results (first time around will be the empty set)
        for i in range(ind, len(nums)):
            tmp_list.append(nums[i])
            self.backtrack(results, tmp_list, nums, i+1) # Increase the index because we already used this current number.
            del tmp_list[-1]




s = Solution()

#print(s.subsets(['a', 'a', 'b']))

print(s.subsets([1, -1, 5, -2, 3]))


