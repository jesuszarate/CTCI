'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def levelOrderBottom(self, root):

        res = []
        q = [root]

        while(q):
            curr_res = []

            l = len(q)

            for i in range(l):
                n = q[0]
                del q[0]

                curr_res.append(n.val)
                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

            res.append(curr_res)
        return res[::-1]

s = Solution()

