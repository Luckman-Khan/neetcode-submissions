class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT, window = {},{}
        for ch in t:
            countT[ch] = 1 + countT.get(ch,0)
        
        l=0
        res,resLen = [-1,-1],float('infinity')
        have,need = 0,len(countT)
        for r in range(len(s)):

            ch = s[r]
            window[ch] = 1 + window.get(ch,0)
            if ch in countT and countT[ch] == window[ch]:
                have+=1
            while need == have:

                if (r-l+1)<resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                
                c = s[l]
                window[c]-=1
                if c in countT and  window[c] < countT[c]:
                    have-=1
                l+=1
            
        left,right = res

        return s[left:right+1] if resLen != float('infinity') else ''

