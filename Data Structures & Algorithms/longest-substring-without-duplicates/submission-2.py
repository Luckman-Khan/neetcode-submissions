class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen = set()
        res=0
        for right in s:
            while right in seen:
                seen.remove(s[left])
                left+=1
            seen.add(right)
            res=max(res,len(seen))
        return res

        