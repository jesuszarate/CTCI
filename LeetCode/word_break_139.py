class Solution1:
    def wordBreak(self, s, wordDict):
        res = [ [None for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        
        for i in range(0, len(s)):
            self.backtrack(res, s, wordDict, [], i, len(s))

        for row in range(len(res)):
            for col in range(len(res[0])):
                if res[row][col]:
                    if self.traverse(res, col):
                        return True
        return False        

    def traverse(self, grid, row):                        
        for col in range(len(grid)):
            if grid[row][col] and col == len(grid) - 1:                        
                return True
        return False

    def backtrack(self, res, s, wordDict, tmp_list, start, end):                
        for i in range(start, end+1):            
            if s[start:i] in wordDict:
                res[start][i] = s[start:i]

s = Solution1()

word = "leetcode"
wordDict = ["leet", "code"]
print(s.wordBreak(word, wordDict))

word = "applepenapple"
wordDict = ["pen", "apple"]
print(s.wordBreak(word, wordDict))

word = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(s.wordBreak(word, wordDict))