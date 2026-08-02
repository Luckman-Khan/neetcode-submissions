class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        for i,height in enumerate(heights):
            start=i
            while stack and stack[-1][1]>height:
                index,poped_height = stack.pop()
                maxArea = max(maxArea,poped_height*(i-index))
                start = index
            stack.append((start,height))
        
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea,(len(heights)-index)*height)
        
        return maxArea