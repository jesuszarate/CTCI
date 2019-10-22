'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        d = dict()
        for i in nums: 
            if i not in d:
                d[i] = 0
            d[i] += 1
            
        res = []        
        for k, v in d.items():
            if v == 1:
                res.append(k)
                
        return res