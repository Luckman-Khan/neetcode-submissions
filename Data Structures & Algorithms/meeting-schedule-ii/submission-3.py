"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
      start = sorted(i.start for i in intervals)
      end = sorted(i.end for i in intervals)

      room = 0
      end_ptr = 0

      for i in range(len(start)):
        if start[i] < end[end_ptr]:
            room+=1
        else:
            end_ptr+=1
      return room 