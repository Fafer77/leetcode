from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_ = 0

        for num in freq:
            if num + 1 in freq:
                max_ = max(max_, freq[num] + freq[num + 1])
        
        return max_
