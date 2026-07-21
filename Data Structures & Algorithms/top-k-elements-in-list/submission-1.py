class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = list(set(nums))
        freq_num=[]
        result =[]
        for num in unique_nums:
            count = nums.count(num)
            freq_num.append((count,num))
        freq_num.sort(reverse=True)

        for i in range(k):
            result.append(freq_num[i][1])
        return result
        