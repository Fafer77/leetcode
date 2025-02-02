from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        mini = min(nums)
        idx_list = [i for i, val in enumerate(nums) if val == mini]
        n = len(nums)
        fails = 0
        for index in idx_list:
            idx = index
            prev = nums[idx]
            for _ in range(1, n):
                idx = (idx + 1) % n
                if prev > nums[idx]:
                    fails += 1
                    break
                prev = nums[idx]

        if fails == len(idx_list):
            return False
        return True
    

sol = Solution()
print(sol.check([6, 10, 6]))
