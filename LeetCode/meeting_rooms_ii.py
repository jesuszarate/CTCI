'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

class Node:
    def __init__(self, val):
        self.val = val # [0, 30]
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node

class Solution:

    def minMeetingRooms(self, intervals):

        rooms = list() # [(), ()]

        for interval in intervals:

            for room in rooms:
                next = self.canSqueezeIn(interval, room)

                if next:
                    self.addToList(next, interval)

                else:
                    new_LL = LinkedList(Node(interval))
                    room.append(new_LL)

        return rooms


    def addToList(self, current_node, interval):
        new_node = Node(interval)

        temp_node = current_node.next

        current_node.next = new_node
        new_node.next = temp_node

        temp_node.prev = new_node
        new_node.prev = current_node

    def canSqueezeIn(self, interval, room):
        '''
        :param interval:
        :param room: Linked List
        :return: Node that will be the next
        '''

        current_room = room.head
        while current_room:

            if self.prev(current_room.val, interval):
               return current_room

            if self.next(current_room.val, interval):
                current_room = current_room.next

        return None





    def prev(self, node, current) -> bool:
        return node[0] >= current[1]

    def next(self, node, current) -> bool:
        return node[1] <= current[0]


s = Solution()

meetings = [[0,30], [15, 20], [5, 10], [10, 15], [0,3], [12,14]]
print(s.minMeetingRooms(meetings))