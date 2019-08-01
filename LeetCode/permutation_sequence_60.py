'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

'''

class Solution:
    '''
    Not the optimal solution. Times out.
    '''
    def getPermutation(self, n, k):

        nums = [i for i in range(1, n+1)]
        result = list()
        visited = [False] * n
        self.backtrack(result, visited, list(), nums, k)
        return "".join([str(i) for i in result[-1]])

    def backtrack(self, result, visited, tmp_lst, nums, k):

        if(len(result) == k):
            return

        if len(tmp_lst) == len(nums):
            result.append([i for i in tmp_lst])
            return

        for i in range(len(nums)):

            if not visited[i]:
                visited[i]  = True
                tmp_lst.append(nums[i])
                self.backtrack(result, visited, tmp_lst, nums, k)
                tmp_lst.pop()
                visited[i] = False


s = Solution()

print(s.getPermutation(4, 9))