class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #nlogn, sort array

        #o(n)
        numSet = set(nums)
        res = 0

        for num in nums:
            #start of a sequence
            if num - 1 not in numSet:
                currLen = 0
                while (num + currLen) in numSet:
                    currLen += 1
                res = max(res, currLen)
        
        return res



        #wrong solution

        # nextNumDict = {}
        # res = []
        # for num in nums:
            
        #     if num not in nextNumDict:
        #         nextNumDict[num] = 1
        #     else:
        #         res.append(nextNumDict[num])
        #         print(num, nextNumDict[num])
        #     nextNumDict[num + 1] = nextNumDict[num] + 1

        # print(nextNumDict)
        # return max(res)
        