import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        # minRes = math.inf
        def binSearch(l , r, nums, minNum):
            mid = l + (r - l) // 2
            print(nums[mid])
            minNum = min(minNum, nums[mid])
            if l > r:
                return minNum
            if nums[mid] > nums[r]:
                return binSearch(mid + 1, r, nums, minNum)
            else:
                return binSearch(l, mid - 1, nums, minNum)


        return binSearch(l, r, nums, math.inf)

        