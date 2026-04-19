class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l , r = 0, len(nums) - 1 

        def binarySearch(l , r, nums, target):
            
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            if l > r:
                return -1
            if (nums[mid] > target and nums[mid] > nums[r]) or (nums[mid] < target and nums[mid] < nums[r]):
                return binarySearch(mid + 1, r, nums, target)
            else:
                return binarySearch(l, mid - 1, nums, target)

        return binarySearch(l , r, nums, target)
        