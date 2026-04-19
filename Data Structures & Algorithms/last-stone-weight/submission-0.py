class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x != y:
                if x < y:
                    heapq.heappush(maxHeap, -y + x)
                else:
                    heapq.heappush(maxHeap, -x + y)
        
        if maxHeap:
            return -heapq.heappop(maxHeap)
        else:
            return 0
            