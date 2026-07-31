class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ""
        for ch in s:

            if ch.isalnum():
                filtered_s += ch
        filtered_s = filtered_s.lower()

        left=0
        right = len(filtered_s)-1

        while left<right:
            if filtered_s[left] != filtered_s[right]:
                return False
            left+=1
            right-=1
        return True