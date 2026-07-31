class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = nums.count(num)
        
        count = sorted(count,key=count.get,reverse=True)
        return count[:k]

        
        