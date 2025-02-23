from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
    
        result = [""] * len(score)

        for rank, (i, _) in enumerate(sorted_scores):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)

        return result


sol = Solution()
print(sol.findRelativeRanks([5,3,7,9]))
