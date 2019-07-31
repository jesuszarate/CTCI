'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
'''

class Solution:
    def __init__(self):
        self.results = set()

    def generateParenthesis(self, n):

        lst = "()"

        self.gp("", lst, n)

        return self.results

    def gp(self, t_lst, lst, n):

        if len(t_lst) == (n*2):
            if self.is_valid(t_lst):
                self.results.add(t_lst)
            return

        for i, p in enumerate(lst):
            t_lst += p
            self.gp(t_lst, lst, n)
            t_lst = t_lst[:-1]

    def is_valid(self, lst):

        stack = []

        for i in lst:

            if i == "(":
                stack.append(i)

            elif i == ")" and len(stack) > 0:
                stack.pop()

            else:
                return False

        return len(stack) == 0








s = Solution()
print(s.generateParenthesis(5))