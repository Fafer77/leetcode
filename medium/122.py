from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prev = prices[0]
        local_low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prev:
                prev = prices[i]
            else:
                max_profit += prev - local_low
                local_low = prices[i]
                prev = prices[i]
        
        return max_profit + prev - local_low