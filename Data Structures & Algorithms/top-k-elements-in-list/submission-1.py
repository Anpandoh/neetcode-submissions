from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        freqList = [[] for x in range(len(nums) + 1)]
        
        #reverse and include empties
        for a, b in count.items():
            freqList[b].append(a)

        res = []
        for i in range(len(freqList) - 1, 0, - 1):
            for items in freqList[i]:
                res.append(items)
                if len(res) == k:
                    return res
        
       