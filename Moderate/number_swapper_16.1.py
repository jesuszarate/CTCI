'''
Write a function to swap a number in place (That is without temporary variables)
'''


def swap(lst):
    lst[0] = lst[0] + lst[1]
    lst[1] = lst[0] - lst[1]
    lst[0] = lst[0] - lst[1]


l = [1, 2]
swap(l)
print(l == [2, 1])

l = [-6, 30]
swap(l)
print(l == [30, -6])
