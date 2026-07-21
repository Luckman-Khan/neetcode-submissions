class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = collections.Counter(nums)

        sorted_nums = sorted(counts.items(),key =lambda item: item[1],reverse = True )

        return [item[0] for item in sorted_nums[:k]] 