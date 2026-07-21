class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left=0
        res = []
        for right in range(k-1,len(nums)):
            maximum = -float("Infinity")
            for wMax in range(left,right+1):
                maximum = max(maximum,nums[wMax])
            res.append(maximum)
            left+=1
        return res
                