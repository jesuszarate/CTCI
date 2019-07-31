'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
    [1,1,2],
    [1,2,1],
    [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        results = list()
        visited = [False] * len(nums)
        self.backtrack(results, list(), nums, visited)
        return results

    def backtrack(self, results, tmp_lst, nums, visited):

        if len(tmp_lst) == len(nums):
            results.append([i for i in tmp_lst])
            return

        for i in range(len(nums)):

            if not visited[i] and self.can_add(visited, nums, i):
                visited[i] = True
                tmp_lst.append(nums[i])
                self.backtrack(results, tmp_lst, nums, visited)
                tmp_lst.pop()
                visited[i] = False

    def can_add(self, visited, nums, pos):
        if pos == 0:
            return True
        return nums[pos - 1] != nums[pos] or visited[pos - 1]



s = Solution()

print(s.permuteUnique([1,1,2]))
