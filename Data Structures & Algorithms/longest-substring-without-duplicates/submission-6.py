class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        left=0
        substring = set()
        maxLength = 1
        for char in s:

            while char in substring:
                substring.remove(s[left])
                left+=1
            substring.add(char)
            maxLength = max(maxLength,len(substring))
        return maxLength
        
