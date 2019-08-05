'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution:

    def partition(self, s):
        result = list()
        self.backtrack(result, "", s, 0)
        return result

    def backtrack(self, result, tmp_s, s, ind):

        current = list()

        # if is_palindrome(tmp_s):
        result.append(tmp_s) # No need to make a full copy here because strings are immutable

        for i in range(ind, len(s)):
            tmp_s += s[i]
            current.append(tmp_s)
            self.backtrack(result, tmp_s, s, i+1)
            tmp_s = tmp_s[-1]

        # if ''.join(current) == s:
        # result.append(current)
        # print(current)

    def is_palindrome(self, s):
        j = len(s) - 1
        if j < 0:
            return False

        for i in range(len(s)//2):
            if s[i] != s[j]:
                return False
        return True

s = Solution()

# print(s.partition("aab"))

l = [0, 1, 2, 3, 4]

print(l)
print(l[::-1])

i = len(l)
print(l[2:4])