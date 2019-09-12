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
        self.val = val  # [0, 30]
        self.next = None
        self.prev = None

    def __str__(self):
        return "(" + self.val[0] + ", " + self.val[1] + ")"

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node


class Solution:

    def minMeetingRooms(self, intervals):

        rooms = list()  # [(), ()]

        for interval in intervals:

            room, node = self.findRoom(rooms, interval)

            self.addToList(rooms[room], node, interval)

        return len(rooms)

    def findRoom(self, rooms, interval):
        for i, room in enumerate(rooms):
            next = self.canSqueezeIn(interval, room)
            if next:
                return (i, next)

        rooms.append(LinkedList(None))
        return (len(rooms) - 1, None)


    def addToList(self, room, current_node, interval):
        new_node = Node(interval)

        if not room.head and not room.tail:
            room.head = new_node
            room.tail = new_node
            return

        if not current_node:
            room.tail = new_node
            new_node.prev = room.tail


        if not current_node.prev:
            room.head = new_node
            new_node.next = current_node


        temp_node = current_node.prev

        current_node.prev = new_node
        new_node.prev = temp_node

        if temp_node:
            temp_node.next = new_node
        new_node.next = current_node


    def canSqueezeIn(self, interval, room):
        '''
        :param interval:
        :param room: Linked List
        :return: Node that will be the next
        '''

        prev_room = None
        current_room = room.head
        while current_room:

            prev = self.prev(current_room.val, interval)
            if prev:
                return current_room

            next = self.next(current_room.val, interval)
            if next:
                prev_room = current_room
                current_room = current_room.next

            if not prev and not next:
                return None
        return prev_room

    def prev(self, node, current) -> bool:
        return node[0] >= current[1]


    def next(self, node, current) -> bool:
        return node[1] <= current[0]


s = Solution()

meetings = [[0, 30], [15, 20], [5, 10], [10, 15], [0, 3], [12, 14]]
meetings = [[0,30],[5,10],[15,20]]
print(s.minMeetingRooms(meetings))
