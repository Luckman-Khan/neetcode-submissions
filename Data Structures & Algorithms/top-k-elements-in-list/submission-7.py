class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = collections.Counter(nums)
        res = sorted(counts.items(),key=lambda item:item[1],reverse=True)
        result = [key for key,_ in res]
        return result[:k]