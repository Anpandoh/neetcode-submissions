class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        res = []
        for i, interval in enumerate(intervals):
            newIntervalStart = newInterval[0]
            newIntervalEnd = newInterval[1]

            start = interval[0]
            end = interval[1]
            if newIntervalEnd < start:
                res.append(newInterval)
                return res  + intervals[i:]
                ##insert, and rest, then return
            
            elif newIntervalStart > end:
                res.append(interval)
                #continue (not the right place to add new interval)
            else:
                #in all intersecting situations just make the new interval the widest mix of the 2
                newInterval = [min(newIntervalStart, start), max(newIntervalEnd, end)]
            
        ##interval includes the end
        res.append(newInterval)
                            
        return res


        