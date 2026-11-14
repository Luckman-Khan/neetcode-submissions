class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxSell = 0
        minBuy = prices[0]

        for sell in prices:

            maxSell = max(maxSell,sell-minBuy)
            minBuy = min(minBuy,sell)
        return maxSell