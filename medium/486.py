from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] has max value of player who is choosing in range (i, j)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        
        # we play mini-games for each length range
        # and then choose maximum possible amount of points that
        # player 1 can have if he starts
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        return dp[0][n-1] >= 0
    


sol = Solution()
print(sol.predictTheWinner([1,5,233,7]))

