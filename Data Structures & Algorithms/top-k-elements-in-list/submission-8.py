class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = collections.Counter(nums)

        sorted_num = sorted(counts.items(),key= lambda items:items[1],reverse=True)
        res = [key for key,value in sorted_num]
        return res[:k]