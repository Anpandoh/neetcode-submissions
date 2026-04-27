import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #lowest numbers
        self.minHeap = [] #highest numbers
        

    def addNum(self, num: int) -> None:
        #min heap maintains the highest numbers
        #max heap maintains the lowest numbers
        ####MAXHEAP####       ####MINHEAP####
        #123456789            101112131415161718  
            #9                      #10

        heapq.heappush_max(self.maxHeap, num) 
        heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))    


        #rebalance (whenever its not alternating amount of numbers)
        if len(self.minHeap) > len(self.maxHeap):
            #if odd index then move the current min of the highest numbers (minHeap) to heap
            heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(self.maxHeap[0])
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2

        
        