'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''


class Solution:

    def minMeetingRooms(self, intervals):
        pass


s = Solution()

meetings = [[0, 30], [15, 20], [5, 10], [10, 15], [0, 3], [12, 14]]
meetings = [[0,30],[5,10],[15,20]]
print(s.minMeetingRooms(meetings))
