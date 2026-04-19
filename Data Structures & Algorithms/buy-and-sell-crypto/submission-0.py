class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l , r = 0 , 0
        maxProfit = 0
        buy = math.inf
        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[r] < buy:
                l = r
                buy = prices[r]
            r += 1
        
        return maxProfit


        