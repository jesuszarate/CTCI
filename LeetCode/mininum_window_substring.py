'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution:
    def minWindow(self, s, t):

        res = list()
        for i in range(len(s)):
            if s[i] in t:
                res.append(i)

        min_ = float("inf")
        lower = -1
        upper = -1
        l = len(t) - 1
        for i in range(len(res) - l):

            val = res[i + l] - res[i]

            if val < min_:
                lower = res[i]
                upper = res[i + l]
                min_ = val

        if (upper - lower) < l :
            return ""

        return s[lower:upper+1]

s = Solution()


print(s.minWindow("bba",
                  "ab"))



