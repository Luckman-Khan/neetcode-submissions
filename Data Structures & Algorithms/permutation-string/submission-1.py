class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False

        s1 = sorted(s1)
        for i in range(len(s2)-len(s1)+1):

            substring = s2[i:i+len(s1)]
            substring = sorted(substring)

            if s1 == substring:
                return True
        
        return False