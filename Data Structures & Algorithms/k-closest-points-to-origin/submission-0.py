class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = abs(pow(pow(x, 2) + pow(y,2), 0.5))
            heapq.heappush(heap, (distance, x, y))

        print(heap)
        kClosest = heapq.nsmallest(k , heap)
        kClosest = [[x,y] for distance, x, y in kClosest]

        return kClosest
         


        