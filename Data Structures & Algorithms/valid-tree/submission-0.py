from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        queue = deque()
        visited = set()
        
        def isTree(node):
            queue.append((node, None))
            visited.add(node)
            while queue:
                currNode, parent = queue.popleft()
                for neighbour in graph[currNode]:
                    if neighbour in visited:
                        if neighbour != parent:
                            return False # not Tree
                    else:
                        visited.add(neighbour)
                        queue.append((neighbour, currNode))
          
            return True # is Tree
        
        return isTree(0) and len(visited) == n
