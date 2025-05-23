from typing import List
from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        @lru_cache(None)
        def dp(i, j):
            if i == n - 1:
                return triangle[i][j]
            return triangle[i][j] + min(dp(i + 1, j), dp(i + 1, j + 1))
        
        return dp(0, 0)
    

    def minimumTotalBetter(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        return triangle[0][0]


sol = Solution()
print(sol.minimumTotal([[-10]]))
