from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for l in range(2, m):
            for i in range(0, m - l):
                j = i + l
                mini = float('inf')
                for k in range(i + 1, j):
                    cand = dp[i][k] + dp[k][j]
                    if cand < mini:
                        mini = cand
                dp[i][j] = mini + cuts[j] - cuts[i]

        return dp[0][m - 1]


sol = Solution()
print(sol.minCost(7, [1,3,4,5]))
