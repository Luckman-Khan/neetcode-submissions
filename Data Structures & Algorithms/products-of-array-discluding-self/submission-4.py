class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)
        pref = 1
        for i,num in enumerate(nums):
            res[i] = pref
            pref *= num
        
        suff=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suff
            suff*=nums[i]
        
        return res
            
        
