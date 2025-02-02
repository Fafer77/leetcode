from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum: int = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target: int = total_sum // 2
        dp: List[bool] = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                if dp[target]:
                    return True
        
        return dp[target]


sol = Solution()
print(sol.canPartition([5, 6, 10, 1]))
