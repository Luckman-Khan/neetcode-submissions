class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        s1 = sorted(s1)
        for right in range(len(s1),len(s2)+1):

            word = sorted(s2[left:right])

            if word == s1:
                return True
            left+=1
        return False


