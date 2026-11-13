class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ''

        for ch in s:
            if ch.isalnum():
                newS += ch.lower()
        return newS == newS[::-1]