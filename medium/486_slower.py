from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        has_cache = [[False] * (n + 1) for _ in range(n + 1)]
        cache = [[None] * (n + 1) for _ in range(n + 1)]

        def score(left, right):
            if left > right:
                return 0
            
            if has_cache[left][right]:
                return cache[left][right]

            score_taking_left = nums[left] - score(left + 1, right)
            score_taking_right = nums[right] - score(left, right - 1)


            has_cache[left][right] = True
            cache[left][right] = max(score_taking_left, score_taking_right)
            return cache[left][right]
        
        return score(0, n - 1) >= 0
        

