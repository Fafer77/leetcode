from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0  # Cała suma już jest podzielna przez p.

        # Mapa przechowująca ostatnie wystąpienia reszt prefixów
        prefix_remainder = {0: -1}
        current_prefix_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            current_prefix_sum = (current_prefix_sum + num) % p
            target_remainder = (current_prefix_sum - remainder) % p

            if target_remainder in prefix_remainder:
                min_length = min(min_length, i - prefix_remainder[target_remainder])

            # Aktualizujemy mapę reszt prefixów
            prefix_remainder[current_prefix_sum] = i

        return min_length if min_length < len(nums) else -1

sol = Solution()
sol.minSubarray([3, 1, 4, 2], 6)