"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        maxMeetings , currMeetings = 0, 0

        s , e = 0 , 0

        while s < len(start) and e < len(end):

            if start[s] < end[e]: #if a meeting starts before curr meeting ends
                s += 1
                currMeetings += 1
            else: #if meeting ends decrement, even if a new meeting starts at same time, that will come in next iteration of loop
                e += 1
                currMeetings -= 1
            maxMeetings = max(maxMeetings, currMeetings)

        return maxMeetings









            




        return maxMeetings

        