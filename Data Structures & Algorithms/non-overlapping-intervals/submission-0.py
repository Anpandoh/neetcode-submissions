class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        initLen = len(intervals)
        #sort the intervals by the first element so we can find overlaps
        intervals.sort(key = lambda x:x[1])

        # go through each interval and find the intersection and remove the one that ends later
        i = 0
        while i < len(intervals) - 1:

            #detect intersection
            if intervals[i][1] > intervals[i+1][0]:
                if intervals[i][1] > intervals[i+1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
            else:
                i += 1
        
        return initLen - len(intervals)


            

