'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

'''
import math


class Solution:
    def kClosest(self, point, K):
        self.lst = point
        self.result = []

        start = 0
        end = len(self.lst) - 1

        self.recClosest(self.lst, K, start, end)
        return self.result

    def recClosest(self, lst, K, start, end):

        if start <= end:
            p = self.partition(lst, start, end)

            if p <= K - 1:
                self.result.append([lst[p][0], lst[p][1]])

            if len(self.lst) == K:
                return

            self.recClosest(lst, K, start, p - 1)
            self.recClosest(lst, K, p + 1, end)

    def partition(self, lst, start, end):

        p = (start + end) // 2  # This would actually be a better pivot
        r = end - 1
        l = start
        self.swap(lst, p, end)

        while l <= r:
            if self.val(l) < self.val(p):
                l += 1

            if self.val(r) > self.val(p):
                r -= 1

            if self.val(l) >= self.val(r):
                self.swap(lst, l, r)
                l += 1
                r -= 1

        self.swap(lst, l, end)
        return l

    def swap(self, lst, l, r):
        lst[l], lst[r] = lst[r], lst[l]

    def val(self, v):
        x1 = self.lst[v][0]
        x2 = self.lst[v][1]

        return math.sqrt((0 - x2) ** 2 + (0 - x1) ** 2)

def value(list, v):
    x1 = list[v][0]
    x2 = list[v][1]

    return math.sqrt((0 - x2) ** 2 + (0 - x1) ** 2)


        #    1     3     2
points = [[3,3],[5,-1],[-2,4]]
# points = [[1,3],[-2,2]]
K = 2

s = Solution()

print(s.kClosest(points, K))

print([value(points, i) for i in range(len(points))])