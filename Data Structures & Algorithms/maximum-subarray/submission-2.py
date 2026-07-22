class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        max_sum = nums[0]
        curr = 0
        
        for num in nums:

            if curr < 0:
                curr = 0

            curr += num
            max_sum = max(curr,max_sum)
        return max_sum


