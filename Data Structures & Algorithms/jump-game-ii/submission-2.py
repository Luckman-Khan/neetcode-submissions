class Solution:
    def jump(self, nums: List[int]) -> int:

        if  len(nums)<=1:
            return 0

        farthest = 0
        current_jump = 0
        count = 0
        for i in range(len(nums)-1):

            if i>farthest:
                return 0
            
            farthest = max(farthest,nums[i]+i)

            if i==current_jump:
                count+=1
                current_jump = farthest
        return count
        