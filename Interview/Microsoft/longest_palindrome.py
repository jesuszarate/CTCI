# Determine Longest palindrome from the random string

#a...a
#aabcbddiaa
#a: 4
#b: 2
#d: 2
#c: 1
#i: 1

# O(n^2)
# max = 5
# aabaaio
#  ^^

# 012
# aba

# ""
# "!&**(()"
# "a"
# "aba*aabbaa*abba"


def findMatch(r_string, current_index): # current_index = 0
    '''
    Return other matching character
    '''
    for i in range(current_index + 1, len(r_string)): # i = 1, 2
        if r_string[i] == r_string[current_index]:
            return i
    return -1

def isPalindrome(r_string, start, end): # 0, 2
    '''
    Determmines if substring is palindrome
    '''
    
    mid = (start + end+1) // 2
    for i in range(start, mid): # i = 1
        # r_string[i] = b
        # r_string[end - i] = b
        if r_string[i] != r_string[end - i]:
            return False
    return True
            

def longestPalindrome(r_string): # aba
    
    max_palindrome = 0 # 3
    for i in range(len(r_string)): # i = 0, 1
        match_i = findMatch(r_string, i) # match_i = 2, -1
        
        if match_i > 0 and isPalindrome(r_string, i, match_i):
            max_palindrome = max(max_palindrome, (match_i - i + 1)) # max(0, 2-0) = 2+1
    
    return max_palindrome
            
    
print(longestPalindrome("aba*aabbaa*abba"))
        
        
        