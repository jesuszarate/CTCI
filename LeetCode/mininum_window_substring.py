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

        T = dict()
        for st in t:
            if st not in T:
                T[st] = 0
            T[st] += 1
        print(T)


s = Solution()

s.minWindow("ADOBECODEBANC", "ABC")



