class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max_volume = 0
        
        while left<right:
            min_height = min(heights[left],heights[right])
            volume = min_height*(right-left)
    
            max_volume = max(volume,max_volume)
        
            if heights[left] > heights[right]:
                right-=1
        
            else:
                left+=1
        
        return max_volume

            

