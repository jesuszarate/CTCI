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

        l = 0
        r = 0

        _min = len(s) + 1
        _l = 0
        _r = 0

        m = dict()
        while r <= len(s) - 1 or len(t) == len(m):
            if len(m) != len(t):
                if s[r] in t:
                    if s[r] not in m:
                        m[s[r]] = 0

                    m[s[r]] += 1
                r += 1
            else:
                if _min > (r - l):
                    _min = (r - l)
                    _l = l
                    _r = r

                if s[l] in m:
                    m[s[l]] -= 1
                    if m[s[l]] == 0:
                        m.pop(s[l])
                l += 1

        return "" if _min > len(s) else s[_l:_r]


s = Solution()


print(s.minWindow("bba",
                  "ab"))

S = "ADOBECODEBANC"
T = "ABC"
print(s.minWindow(S, T))

S = "a"
T = "a"
print(s.minWindow(S, T))

S = "a"
T = "b"
print(s.minWindow(S, T))


S = "aa"
T = "aa"
print(s.minWindow(S, T))

