from math import sqrt, floor

class Solution:
    def pickGifts(self, gifts, k):
        for i in range(k):
            max_pile = max(gifts)
            max_index = gifts.index(max_pile)
            gifts[max_index] = floor(sqrt(max_pile))

        print(gifts)
        return sum(gifts)

sol = Solution()
print(sol.pickGifts([1, 1, 1, 1], 4))
