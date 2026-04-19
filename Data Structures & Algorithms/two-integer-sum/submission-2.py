class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #doesn't work because input can be negative
        # l  = 0
        # r = len(nums) - 1

        # while l < r:
        #     if nums[l] + nums[r] == target:
        #         return [l , r]
        #     elif nums[l] + nums[r] > target:
        #         r -= 1
        #     else:
        #         l += 1

        found = {}
        for i, num in enumerate(nums):
            if target - num in found:
                return [found[target - num], i]
            found[num] = i

