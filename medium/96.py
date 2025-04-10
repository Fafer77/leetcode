from math import comb

class Solution:
    def numTrees(self, n: int) -> int:
        return int(1 / (n + 1) * comb(2*n, n))
