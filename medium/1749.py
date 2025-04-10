from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # max sum
        max_sum = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            elif curr_sum < 0:
                curr_sum = 0
        
        min_sum = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum < min_sum:
                min_sum = curr_sum
            elif curr_sum > 0:
                curr_sum = 0
        
        return max(abs(min_sum), max_sum)


sol = Solution()
print(sol.maxAbsoluteSum([2,-5,1,-4,3,-2]))
