class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        

        kLargest = heapq.nlargest(k, heap)

        return kLargest.pop(-1)
        