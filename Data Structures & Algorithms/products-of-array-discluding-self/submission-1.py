class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            product = 1
            for x in range(len(nums)):
                if x!= i:
                    product *= nums[x]
            arr.append(product)
        return arr

        