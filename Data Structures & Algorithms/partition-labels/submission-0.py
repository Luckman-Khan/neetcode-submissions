class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index = {}
        for i,ch in enumerate(s):
            last_index[ch] = i
        
        res = []
        size = 0
        end = 0
        for i,ch in enumerate(s):
            size+=1
            end = max(end,last_index[ch])

            if i == end:
                res.append(size)
                size = 0
                end = 0
            
        return res
