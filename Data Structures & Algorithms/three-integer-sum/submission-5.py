class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = []
        for i in range(n-2):

            left = i+1
            right= n-1

            while left<right:
                Sum = nums[left]+nums[right]

                if Sum == -nums[i]:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                
                elif Sum< -nums[i]:
                    left+=1
                else:
                    right-=1
                
        unique_res = [list(item) for item in set(tuple(row) for row in result)]
        return unique_res