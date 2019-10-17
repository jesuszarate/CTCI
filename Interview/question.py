'''

Given any two lists, each containing key-value pairs, generate a new list that has actions needed to convert first list
into the second one. Example
A is [[‘a’, 3], [‘b’, 2]] and
B is [[‘b’, 4], [‘c’, 10]],

to convert A into B we need
[[‘a’, ‘delete’], [‘b’, ‘update’, 4], [‘c’, ‘create’, 10]]. Order of actions doesn’t matter.
'''


def convert(A, B):

    actions = []
    for a in A:
        value = contains(B, a)
        if value:
            if value[1] != a[1]:
               actions.append([a[0], 'update', value[1]])
        else:
            actions.append([a[0], 'delete'])

    for b in B:
        actions.append([b[0], 'create', b[1]])

    return actions


def contains(B, element):
    # Remove element from B
    for i in range(len(B)):
        b = B[i]
        if element[0] == b[0]:
            del B[i]
            return b


print(convert([['a', 3], ['b', 2]], [['b', 4], ['c', 10]]))
print(convert([], [['b', 4], ['c', 10]]))
print(convert([['a', 3], ['b', 2]], []))
print(convert([], []))

##########################
#         notes          #
##########################
'''
Behavioural 


'''