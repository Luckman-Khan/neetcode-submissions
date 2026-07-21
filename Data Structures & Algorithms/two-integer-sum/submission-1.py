class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_nums= nums[:i]+nums[i+1:]
            for j in range(len(new_nums)):
                if nums[i]+new_nums[j]==target:
                    return [i,j+1]
                    
