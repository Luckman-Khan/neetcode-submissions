class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum = nums[left]+nums[right]
                if sum == -nums[i]:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif sum < -nums[i]:
                    left+=1
                elif sum > -nums[i]:
                    right-=1
        unique_result = [list(item) for item in set(tuple(row) for row in result)]
        return unique_result
                
            



