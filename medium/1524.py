from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        sum_ = 0
        odd_sum_count = 0
        even_sum_count = 0
        total_odd_sum = 0
        for x in arr:
            sum_ += x
            if sum_ % 2 == 0:
                even_sum_count += 1
                total_odd_sum += odd_sum_count
            else:
                odd_sum_count += 1
                total_odd_sum += even_sum_count + 1
                    
        return total_odd_sum % MOD
    
sol = Solution()
print(sol.numOfSubarrays([1,2,3,4,5,6,7]))
