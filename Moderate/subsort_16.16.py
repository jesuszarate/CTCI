class Solution:
    '''
    Given an array of integers, write a method to find indices m and n suc that if you sorted elements m through n, the entire array would be sorted. 
    Minimize n - m (that is find the smallest such sequence).

    Input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    Output: (3, 9) 
    '''

    def subsort(self, lst):

        left = 0
        right = len(lst)

        left = self.unsortedLeftIndex(lst)
        right = self.unsortedRightIndex(lst)
        
        max_index = left
        min_index = right

        for i in range(left, right+1):
            if lst[max_index] < lst[i]:
                max_index = i
            if lst[min_index] > lst[i]:
                min_index = i            
        
        left_index = self.shrinkLeft(lst, min_index)
        right_index = self.shrinkRight(lst, max_index)
        
        return (left_index, right_index-1)

    def shrinkLeft(self, lst, left):
        l_value = lst[left]
        left -= 1
        while l_value < lst[left]:
            left -= 1
        return left

    def shrinkRight(self, lst, right):
        r_value = lst[right]
        right += 1
        while r_value > lst[right]:
            right += 1
        return right

    def unsortedLeftIndex(self, lst):        
        for i in range(1, len(lst) - 1):
            if lst[i-1] > lst[i]:
                return i
        return -1

    def unsortedRightIndex(self, lst):    
        for i in range(len(lst) - 2, -1, -1):
            if lst[i+1] < lst[i]:
                return i
        return -1

s = Solution()        
print(s.subsort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))