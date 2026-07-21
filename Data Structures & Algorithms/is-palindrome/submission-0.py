class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = s[::-1]
        newS=''
        for c in s:
            if c.isalnum():
                newS += c.lower()
        return newS == newS[::-1]