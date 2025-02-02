from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(v, path):
            for u in graph[v]:
                if u == n:
                    paths.append(path + [u])
                path.append(u)
                dfs(u, path)
                path.pop()

        n = len(graph) - 1
        paths = []
        dfs(0, [0])
        return paths


sol = Solution()
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))


