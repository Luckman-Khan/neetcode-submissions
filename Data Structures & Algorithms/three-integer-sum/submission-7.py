class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n-2):

            left=i+1
            right=n-1

            while left<right:

                if (nums[i]+nums[left]+nums[right])==0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                
                elif (nums[left]+nums[right])<-nums[i]:
                    left+=1
                else:
                    right-=1
                
        result = []
        for triplet in res:
            if triplet in result:
                continue
            else:
                result.append(triplet)
        
        return result
                    