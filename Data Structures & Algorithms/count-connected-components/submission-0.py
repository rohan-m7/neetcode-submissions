from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()

        def dfs(node):
            visit.add(node)
            for adj in graph[node]:
                if adj not in visit:
                    dfs(adj)
        
        compnonents = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                compnonents += 1
        return compnonents
            
            