'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?

'''

'''
[1, -1, 5, -2, 3], k = 3

[-2, -1, 1, 3, 5]

 1, -1, 5, -2, 3
 1, -1, 5, -2
 1, -1, 5
 1, -1
 1
 
-1, 5, -2, 3
-1, 5, -2,
-1, 5
-1

 5, -2, 3
 5, -2
 5
 
 -2, 3
 -2
 
 3


'''

class Solution:
    def __init__(self):
        self.mx = -float("inf")

    def maxSubArrayLen(self, nums, k):
        lst = list()
        lst.sort()
        self.backtrack(lst, list(), nums, 0, len(nums), k)

        return self.mx

    def backtrack(self, ans, tmp, nums, start, end, k):
        if sum(tmp) == k:
            self.mx = max(len(tmp), self.mx)
            ans.append(tmp[:])

        for i in range(start, end):
            if i > start and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            self.backtrack(ans, tmp, nums, i+1, end, k)
            tmp.pop()



s = Solution()

print(s.maxSubArrayLen([1, -1, 5, -2, 3],3))






