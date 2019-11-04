class Solution:
    def rob(self, nums):

        cache = dict()
        self.max = 0

        for i in range(len(nums)):
            self.robRec(nums, i, cache)

        return self.max

    def robRec(self, nums, n, cache):

        if n >= len(nums):
            return 0

        if n in cache:
            return cache[n]

        m = max(self.robRec(nums, n+2, cache),
                self.robRec(nums, n+3, cache)) + nums[n]

        self.max = max(self.max, m)
        cache[n] = m

        return m


s = Solution()

print(s.rob([1, 2]))
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
