class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []
        #O(n^2), basically go through each num, and run a 2 pointer for the last 2 numbers
        for i, num in enumerate(nums):
            
            #skip if the num is duplicate
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                triple = num + nums[l] + nums[r]

                if triple == 0:
                    res.append([num, nums[l] , nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif triple > 0:
                    r -= 1
                elif triple < 0:
                    l += 1

        

        return res