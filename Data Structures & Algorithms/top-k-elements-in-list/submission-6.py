class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = collections.Counter(nums)
        res = sorted(counts,key= lambda x:counts[x],reverse=True)

        return res[:k]