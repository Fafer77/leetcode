from typing import List

INF = 10**9

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        rows = len(coins) + 1
        cols = amount + 1
        dp = [[0] * (cols) for _ in range(rows)]
        for i in range(1, cols):
            dp[0][i] = INF
        
        for j in range(rows):
            dp[j][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                exclude = dp[i-1][j]
                include = INF
                if j - coins[i-1] >= 0:
                    include = 1 + dp[i][j-coins[i-1]]
                dp[i][j] = min(exclude, include)

        return dp[-1][-1] if dp[-1][-1] < INF else -1


sol = Solution()
print(sol.coinChange([2], 3))
        