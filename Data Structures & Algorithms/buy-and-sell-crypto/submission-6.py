class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0,1
        maxP = 0
        while right<len(prices):
            price = prices[right]-prices[left]
            if price>0:
                maxP = max(maxP,price)
            else:
                left=right
            right+=1
        return maxP
