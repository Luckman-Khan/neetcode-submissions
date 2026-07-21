class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n-2):

            left = i+1
            right = n-1

            while left<right:
                if (sorted_nums[left] + sorted_nums[right]+sorted_nums[i]) == 0:
                    result.append([sorted_nums[left],sorted_nums[right],sorted_nums[i]])
                    left+=1
                    right-=1
                elif (sorted_nums[left] + sorted_nums[right]) < -sorted_nums[i]:
                    left+=1
                else:
                    right-=1

        res = []
        for item in result:
            if item in res:
                continue
            else:
                res.append(item)

        return res       