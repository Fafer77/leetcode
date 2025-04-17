from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0] * n
        sell = [0] * n
        wait = [0] * n
        hold[0] = -prices[0]
        sell[0], wait[0] = 0, 0

        for i in range(1, n):
            hold[i] = max(hold[i - 1], wait[i - 1] - prices[i])
            sell[i] = hold[i - 1] + prices[i]
            wait[i] = max(sell[i - 1], wait[i - 1])
        
        max_ = max(hold[n - 1], sell[n - 1], wait[n - 1])
        return max_ if max_ > 0 else 0