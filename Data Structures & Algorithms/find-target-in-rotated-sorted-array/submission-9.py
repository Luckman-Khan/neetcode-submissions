class Solution:

    def binarySearch(self,nums:List[int],target:int)->int:

        left,right=0,len(nums)-1
        print(*nums)
        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

    def search(self, nums: List[int], target: int) -> int:

        i=1
        while i<len(nums) and nums[i-1]<nums[i]:
            i+=1
        
        part1 = nums[0:i]
        part2 = nums[i:]

        res1 = self.binarySearch(part1,target)
        res2 = self.binarySearch(part2,target)
        

        if res1!=-1:
            return res1
        elif res2!=-1:
            return (len(part1)+res2)
        else:
            return -1        
        

    

                 