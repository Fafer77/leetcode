from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        n = len(colors)

        max_cost = neededTime[0]
        for i in range(1, n):
            if colors[i-1] == colors[i]:
                if max_cost < neededTime[i]:
                    total_cost += max_cost
                    max_cost = neededTime[i]
                else:
                    total_cost += neededTime[i]
            else:
                max_cost = neededTime[i]

        return total_cost

sol = Solution()
print(sol.minCost('"aaabbbabbbb"', [3,5,10,7,5,3,5,5,4,8,1]))
