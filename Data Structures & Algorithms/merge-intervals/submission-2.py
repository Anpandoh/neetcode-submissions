class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])

        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        res = [[prevStart, prevEnd]]
        for interval in intervals[1:]:

            if prevEnd >= interval[0]:
                res.pop(-1)
                res.append([prevStart, max(prevEnd, interval[1])])
                prevEnd = max(prevEnd, interval[1])
            else:
                res.append(interval)
                prevStart = interval[0]
                prevEnd = interval[1]

        return res




        