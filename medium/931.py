from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf') for _ in range(n + 2)] for _ in range (n)]
        for i in range(n):
            dp[n - 1][i + 1] = matrix[n - 1][i]

        # process to get the best value
        for i in range(n - 2, -1, -1):
            for j in range(n):
                dp[i][j + 1] = matrix[i][j] + min(dp[i+1][j+1], dp[i+1][j], dp[i+1][j+2])
        
        return min(dp[0])


sol = Solution()
print(sol.minFallingPathSum([[-19,57],[-40,-5]]))
