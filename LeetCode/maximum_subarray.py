'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide 
and conquer approach, which is more subtle.
'''


class Solution:

    def maxSubArray(self, lst):
        currentSum = lst[0]
        maxSum = lst[0]

        for i in range(1, len(lst)):

            c = currentSum + lst[i]

            if c < lst[i]:
                currentSum = lst[i]
            else:
                currentSum = c

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum


s = Solution()

print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-1, -2]))
