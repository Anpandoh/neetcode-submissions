class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxElements = []
        for i in range(len(nums)- k +1):
            # print(f"i {i}")

            currMax = float("-inf")
            for x in range(k):
                # print(nums[i+x])
                currMax = max(currMax, nums[i+x])
            
            maxElements.append(int(currMax))


        

        return maxElements
            
        