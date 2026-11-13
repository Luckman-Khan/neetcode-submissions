class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = sorted(nums)
        count = 1
        maxCount = 1
        for i in range(1,len(nums)):
        
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                count+=1
            else:
                maxCount = max(count,maxCount)
                count = 1
        return max(maxCount,count)