class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        sorted_nums = sorted(nums)
        count = 1  
        maxC = 1
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue  
                
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                count += 1  
            else:
                maxC = max(maxC, count)  
                count = 1  
                
        return max(maxC, count)