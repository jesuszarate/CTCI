'''

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

class Solution:
    def topKFrequent(self, nums, k):
        res = dict()
        for i in nums:
            if i not in res:
                res[i] = 0
            res[i] += 1

        vals = []
        for key, val in res.items():
            vals.append((key, val))

        vals = sorted(vals, reverse=True, key=lambda x: x[1])
        return [vals[i][0] for i in range(k)]


s = Solution()
print(s.topKFrequent([3,0,1,0], 1))