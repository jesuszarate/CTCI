'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root):
        self.min = float("inf")
        self.getMinimumDiffRec(root, [root.val])
        return self.min

    def getMinimumDiffRec(self, root, path):
        if root.left:
            self.checkMin(path, root.left.val)
            path.append(root.left.val)
            self.getMinimumDiffRec(root.left, path)
            path.pop()

        if root.right:
            self.checkMin(path, root.right.val)
            path.append(root.right.val)
            self.getMinimumDiffRec(root.right, path)
            path.pop()

    def checkMin(self, path, val):
        for v in path:
            self.min = min(self.min, abs(val - v))
