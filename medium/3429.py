from typing import List

class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        k = n//2
        pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
        dp = [[[float('inf') for _ in range(3)] for _ in range(3)] for _ in range(k)]

        for (x, y) in pairs:
            dp[0][x][y] = cost[0][x] + cost[n - 1][y]
        
        for m in range(1, k):
            for x, y in pairs:
                best = float('inf')
                for i, j in pairs:
                    if x == i or y == j:
                        continue
                    cand = dp[m-1][i][j] \
                    + cost[m][x] \
                    + cost[n - 1 -m][y]
                    if cand < best:
                        best = cand
                dp[m][x][y] = best
        
        return min(dp[k - 1][x][y] for x, y in pairs)



sol = Solution()
print(sol.minCost(4, [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]))
