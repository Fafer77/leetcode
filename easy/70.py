class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2, 0]
        for i in range(2, n):
            dp[2] = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = dp[2]
        
        return dp[2]


sol = Solution()
print(sol.climbStairs(10))
