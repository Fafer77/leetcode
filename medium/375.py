class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 0
        
        for i in range(1, n):
            dp[i][i + 1] = i

        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1 # end of range

                for k in range((i + j) // 2, j):
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[1][n]
