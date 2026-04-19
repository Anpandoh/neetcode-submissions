"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if intervals:
            intervals.sort(key = lambda x:x.start)
            prevStart = intervals[0].start
            prevEnd = intervals[0].end


            for intervals in intervals[1:]:
                currStart = intervals.start
                currEnd = intervals.end
                if prevEnd > currStart:
                    return False
                prevStart = currStart
                prevEnd = currEnd
        return True


