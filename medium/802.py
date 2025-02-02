from typing import List

# terminal node i -> empty graph[i]
# safe node i -> if every path from i leads to terminal node (or another safe node)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe_nodes = []
        color = [0] * n

        for v in range(n):
            if graph[v] is None:
                color[v] = 2
        
        def dfs(v):
            if color[v] > 0:
                return color[v] == 2
            color[v] = 1
            for u in graph[v]:
                if color[u] == 2:
                    continue
                if color[u] == 1 or not dfs(u):
                    return False
            color[v] = 2
            return True
        
        for i in range(n):
            if color[i] != 2:
                if dfs(i):
                    safe_nodes.append(i)
            else:
                safe_nodes.append(i)
        
        return sorted(safe_nodes)



