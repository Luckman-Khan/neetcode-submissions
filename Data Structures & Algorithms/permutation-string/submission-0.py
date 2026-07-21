class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,  m = len(s1),len(s2)
        if n>m:
            return False
        countS = {}
        countWindow = {}

        for r in s1:
            countS[r] = 1 + countS.get(r,0)
        
        for r in s2[:n]:
            countWindow[r] = 1 + countWindow.get(r,0)
         
        if countS == countWindow:
            return True
        
        for i in range(n, m):
          countWindow[s2[i]] = 1 + countWindow.get(s2[i], 0)
          old = s2[i-n]
          countWindow[old] -= 1
          if countWindow[old] == 0:
             del countWindow[old]
          if countWindow == countS:
            return True

        return False