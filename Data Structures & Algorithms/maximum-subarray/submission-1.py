class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        n = len(nums)
        res = nums[0]
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                res = max(res,current_sum)
        return res


