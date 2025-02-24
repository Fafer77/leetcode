from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        bob_time = [float('inf')] * n
        def dfs_bob(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            for neighbor in adj[node]:
                if neighbor != parent:
                    if dfs_bob(neighbor, node, time + 1):
                        bob_time[node] = time
                        return True
            return False
        dfs_bob(bob, -1, 0)

        max_income = float('-inf')
        def dfs_alice(node, parent, time, income):
            nonlocal max_income
            if time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2

            if node != 0 and len(adj[node]) == 1:
                max_income = max(max_income, income)
                return

            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs_alice(neighbor, node, time + 1, income)

        dfs_alice(0, -1, 0, 0)

        return max_income

sol = Solution()
print(sol.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))
