from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        #we want to process the most frequent tasks first
        heap = Counter(tasks)
        heap = [(-value, key) for key, value in heap.items()]
        heapq.heapify(heap)
        print(heap)
        time = 0
        q = []
        while heap or q:
            time += 1
            if heap:
                amountLeft, task = heapq.heappop(heap)
                if amountLeft != -1:
                    q.append((amountLeft + 1, time + n, task))
            if q and time == q[0][1]:
                heapq.heappush(heap, (q.pop(0)[0], task))

        
        return time


        
            




