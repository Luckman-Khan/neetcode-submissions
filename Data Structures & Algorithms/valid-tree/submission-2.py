class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}

        for num1,num2 in edges:
            adj[num1].append(num2)
            adj[num2].append(num1)
        
        visit=set()
        def dfs(i,prev):

            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j==prev:
                    continue
                
                if not dfs(j,i):
                    return False
                
            return True
            
        return dfs(0,-1) and len(visit)==n