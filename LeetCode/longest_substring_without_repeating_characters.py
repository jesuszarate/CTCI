'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

MY Work:

abcabcbb
bbcbacba
11223333

pwwkew
121233

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 1
        cache = list()
        cache.append(1)

        for i in range(1, len(s)):

            cache.append(self.getSubstring(s, i, cache[i - 1], s[i]))
            mx = max(cache[i], mx)

        return 0 if s == '' else mx

    def getSubstring(self, s, start, k, val):

        count = 1
        for i in range(start-1, start - k - 1, -1):

            if s[i] == val:
                return count
            count += 1

        return count

s = Solution()

string = "abcpabcbb"
print(s.lengthOfLongestSubstring(string))# == 3)

string = "pwwkew"
print(s.lengthOfLongestSubstring(string))# == 3)

string = "bbbbb"
print(s.lengthOfLongestSubstring(string))# == 1)

string = ""
print(s.lengthOfLongestSubstring(string))# == 0)