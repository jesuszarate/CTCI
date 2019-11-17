'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x):
        '''
        "4"
        "2*2"
        "3*3"
        
        9/2 = 4"
        4*4 = 16" Too high
        
        4/2 = 2"
        2*2 = 4" Too low
        
        (2 + 4) / 2 = 3"
        3*3 = 9 Found
        '''
        
        low = 0
        high = x
        
        while low <= high:
                        
            mid = (low + high)//2            
            squared = mid**2
            
            if squared == x:
                return int(mid)            
            elif squared < x:
                low = mid + 1      
            else:
                high = mid - 1  
        
        return (low + high)//2
            
            