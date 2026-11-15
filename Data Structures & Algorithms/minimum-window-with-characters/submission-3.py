class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t=='':
            return ''
        left=0
        need = len(t)
        substring = ''
          
        res = [-1,-1]
        resLen = float('infinity')
        countT,window = {},{}
        
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)
        have = 0
        need = len(countT)

        for right in range(len(s)):

            ch = s[right]
            window[ch] = 1 + window.get(ch,0) 
            if ch in countT and countT[ch] == window[ch]:
                have+=1
            
            while have==need:
                if(right-left+1)<resLen:
                    res = [left,right]
                    resLen = right-left+1
                window[s[left]]-=1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have-=1
                left+=1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""
            
