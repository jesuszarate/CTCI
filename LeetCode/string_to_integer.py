'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
'''

class Solution:
    def myAtoi(self, string):

        '''

        Walk through the string starting on the left.
        Taking the digit from chart to int, and then multiplying by 10^ith
        If at any point the number goes above 2^32 or

        :param str:
        :return:
        '''

        # −2^31,  2^31 − 1

        string = self.getOnlyNumbers(string)

        if len(string) > 0 and not self.isInteger(string[0]) and string[0] != '-':
            return 0

        pos = len(string) - 1
        current = 0
        value = 0
        negative = False
        while current < len(string):
            val = string[current]

            if val == '-':
                negative = True
                current += 1
                pos -= 1
                continue

            if not self.isInteger(val):
                break

            value += self.charToInt(val) * 10**pos
            current += 1
            pos -= 1

        return value * -1 if negative else value

    def isInteger(self, c):
        return ord(c) > 48 and ord(c) < 58

    def charToInt(self, c):
        if self.isInteger(c):
            return ord(c) - 48
        else:
            return 0

    def getOnlyNumbers(self, string):
        string = string.strip()
        s = ""
        for i in range(len(string)):

            if not self.isInteger(string[i]) and string[i] != '-':
                return s
            s += string[i]
        return s

s = Solution()

print(s.myAtoi("-4193 with words"))
print(s.myAtoi("words and 987   "))
print(s.myAtoi("    -4193 with words"))