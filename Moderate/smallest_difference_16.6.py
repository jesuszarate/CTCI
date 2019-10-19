'''
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each array)
with the smallest (non-negative) difference. Return the difference.

Example:
Input: 
    [1, 3, 15, 11, 2]
    [23, 127, 235, 19, 8]
'''


def getMax(g_max, c_max):

    if g_max[0] == float("inf"):
        return c_max

    if abs(g_max[0] - g_max[1]) > abs(c_max[0] - c_max[1]):
        return c_max
    return g_max


def smallest_difference(a1, a2):

    a1.sort()
    a2.sort()
    a3 = []

    p1 = p2 = 0

    prev = 1 if a1[0] < a2[0] else 2
    g_max = (float("inf"), float("inf"))

    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] < a2[p2]:
            if prev == 2:
                g_max = getMax(g_max, (a3[-1], a1[p1]))
            a3.append(a1[p1])
            prev = 1
            p1 += 1
        else:
            if prev == 1:
                g_max = getMax(g_max, (a3[-1], a2[p2]))
            a3.append(a2[p2])
            prev = 2
            p2 += 1

    return g_max


print(smallest_difference([1, 3, 15, 11, 2],
                          [23, 127, 235, 19, 8]))
