'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution:
    def findKthLargest(self, nums, k):
        return self.find(nums, 0, len(nums) - 1, k)

    def find(self, nums, start, end, k):
        p = self.partition(nums, start, end)
        if len(nums) - k == p:
            return nums[p]
        elif len(nums) - k < p:
            return self.find(nums, start, p - 1, k)
        else:
            return self.find(nums, p + 1, end, k)

    def partition(self, nums, start, end):

        pivot = self.pivot(start, end)
        self.swap(nums, end, pivot)

        left = start
        right = end - 1

        while left < right:

            if nums[left] < nums[pivot]:
                left += 1

            if nums[right] > nums[pivot]:
                right -= 1

            if nums[left] > nums[right]:
                self.swap(nums, left, right)
                left += 1
                right -= 1

        self.swap(nums, left, end)
        return left


    def pivot(self, low, high):
        return (low + high) // 2

    def swap(self, arr, p1, p2):
        arr[p1], arr[p2] = arr[p2], arr[p1]

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 3))