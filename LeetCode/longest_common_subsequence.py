'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        res1 = set()
        res2 = set()

        self.backtrack(res1, text1, "", 0)        
        self.backtrack(res2, text2, "", 0)


        mx = 0
        for ss in res1:            
            if ss in res2:
                mx = max(mx, len(ss))
        return mx

    def backtrack(self, res, text, tmp, ind):
        res.add(tmp)                

        for i in range(ind, len(text)):
            tmp += text[i]
            self.backtrack(res, text, tmp, i+1)
            tmp = tmp[:-1]

s = Solution()        

text1 = "abcde"
text2 = "ace"
print(s.longestCommonSubsequence(text1, text2))

