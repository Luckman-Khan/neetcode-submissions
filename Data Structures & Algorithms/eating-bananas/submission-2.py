class Solution:
    def time(self,piles: List[int], h: int, k: int) -> int:
        total = 0
        for pile in piles:

            total+=(pile+k-1)//k
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        left,right = 1,max(piles)
        ans = right
        while left<=right:
            k=(left+right)//2
            total = 0
            for pile in piles:
                 total+=(pile+k-1)//k
            
            if total<=h:
                ans = k
                right = k-1
            else:
                left = k+1
        return ans

    

