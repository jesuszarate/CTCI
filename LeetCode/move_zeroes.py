class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        
        [0, 1, 0, 3, 12]
         ^  ^
         0 1
         1, 0, 0, 3, 12
            ^        ^
         1, 3, 0, 0, 12
               ^      ^
         1, 3, 12, 0, 0
        '''
        
        zero = 0
        number = 0
        while zero < len(nums) and number < len(nums):            
            if nums[zero] != 0:
                zero += 1
                number += 1
                continue
                
            if nums[number] == 0:
                number += 1
                continue
                
            if nums[zero] == 0 and nums[number] != 0:
                nums[zero], nums[number] = nums[number], nums[zero]
            
        
        print(nums)
            

s = Solution()
s.moveZeroes([4,2,4,0,0,3,0,5,1,0])                                    