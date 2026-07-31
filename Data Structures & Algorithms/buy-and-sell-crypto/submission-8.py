class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        maxPrice = 0

        for sell in prices:
            maxPrice = max(sell-minBuy,maxPrice)
            minBuy = min(sell,minBuy)
        
        return maxPrice
        