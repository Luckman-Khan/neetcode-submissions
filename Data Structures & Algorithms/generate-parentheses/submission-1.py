class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s:str,open:int,close:int):

         if 2*n == len(s):
            res.append(s)
            return
         if open<n:
            dfs(s+'(',open+1,close)
         if close<open:
            dfs(s+')',open,close+1)
        dfs('',0,0)
        return res
