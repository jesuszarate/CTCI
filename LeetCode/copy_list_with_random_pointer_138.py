'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



Example 1:
     1
    . \
   2 . 2

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


Note:

You must return the copy of the given head as a reference to the cloned list.
'''

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        visited = dict()
        return self.deepCopy(head, visited)

    def deepCopy(self, node, visited):

        if not node:
            return None


        new_node = Node(node.val, None, None)
        visited[node] = new_node

        if node.next:
            new_node.next = self.deepCopy(node.next, visited)

        if node.random:
            if node not in visited:
                new_node.random = self.deepCopy(node.random, visited)
            else:
                new_node.random = visited[node.random]

        return new_node



