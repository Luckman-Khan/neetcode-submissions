class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        maxArea = 0
        for i in range(len(heights)):
            height = heights[i]

            right=i+1
            while right<len(heights) and heights[right]>=height:
                right+=1
            left=i
            while left>=0 and heights[left]>=height:
                left-=1
            right-=1
            left+=1
            
            maxArea = max(maxArea,height*(right-left+1))
        
        return maxArea