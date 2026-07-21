class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     unique_nums = list(set(nums))
     result=[]
     frequency_nums=[]
     for num in unique_nums:
        count = nums.count(num)
        frequency_nums.append((count,num))
     frequency_nums.sort(reverse=True)
    
     for i in range(k):
        result.append(frequency_nums[i][1])
     return result


