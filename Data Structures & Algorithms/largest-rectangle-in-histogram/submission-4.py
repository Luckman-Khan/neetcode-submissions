class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        for i,height in enumerate(heights):
            start=i
            while stack and stack[-1][1]>height:
                index,poped_height = stack.pop()
                maxArea = max(maxArea,(i-index)*poped_height)
                start = index
            stack.append((start,height))

        for i,height in stack:
            maxArea = max(maxArea,(len(heights)-i)*height)
        
        return maxArea