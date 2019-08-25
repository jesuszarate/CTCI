'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):

        lst = []
        self.getAsList(root, lst)

        for i in range(len(lst)):
            if lst[i] != lst[(i + 1)*-1]:
                return False
        return True

    def getAsList(self, root, result):

        if root:
            self.getAsList(root.left, result)

            result.append(root.val)

            self.getAsList(root.right, result)


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(2)

print(s.isSymmetric(root) == False)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(s.isSymmetric(root) == True)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.righ = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

print(s.isSymmetric(root) == False)