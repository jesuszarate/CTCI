'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
'''


class Solution:
    def kConcatenationMaxSum(self, arr, k):

        g_max = elements_so_far = 0

        for _ in range(k):
            for x in arr:
                elements_so_far = max(x, elements_so_far + x)
                g_max = max(g_max, elements_so_far)

        print(g_max)


s = Solution()

print(s.kConcatenationMaxSum([1, 2], 3))
