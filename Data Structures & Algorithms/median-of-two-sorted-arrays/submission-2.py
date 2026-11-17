class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for num in nums2:
            nums1.append(num)
        
        print(nums1)
        nums1.sort()
        n = len(nums1)-1
        if n%2==0:
            return nums1[(n+1)//2]
        else:
            return (nums1[n//2]+nums1[(n+1)//2])/2