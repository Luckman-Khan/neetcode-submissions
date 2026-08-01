class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left= 0
        res = []
        for right in range(k,len(nums)+1):

            substring = nums[left:right]
            res.append(max(substring))
            left+=1
        return res