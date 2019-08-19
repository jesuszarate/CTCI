# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):

        q = [root]
        l = 1
        sums = []

        while q:

            sm = 0
            for i in range(l):

                c = q[0]
                del q[0]

                sm += c.val

                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)

            sums.append(sm/l)
            l = len(q)

        return sums



s = Solution()

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

r = s.averageOfLevels(root)
print(r)
        