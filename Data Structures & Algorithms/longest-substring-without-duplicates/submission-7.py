class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        seen = set()
        maxSubstring = 0
        for ch in s:

            while ch in seen:
                seen.remove(s[left])
                left+=1
            seen.add(ch)
            maxSubstring = max(maxSubstring,len(seen))
        return maxSubstring
