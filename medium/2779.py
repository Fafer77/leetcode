from collections import defaultdict

class Solution:
    def maximumBeauty(self, nums, k):
        if len(nums) == 1 and k <= 1:
            return 1

        nums.sort()
        max_beauty = 0
        left, right = 0, 1
        while right < len(nums):
            if nums[right] - nums[left] <= 2 * k:
                right += 1
                max_beauty = max(max_beauty, right - left)
            else:
                left += 1
        return max_beauty


    # def maximumBeauty(self, nums, k):
    #     range_count = defaultdict(int)
    #     for num in nums:
    #         range_count[num - k] += 1
    #         range_count[num + k + 1] -= 1
        
    #     max_beauty = 0
    #     curr_beauty = 0
    #     for key in sorted(range_count.keys()):
    #         curr_beauty += range_count[key]
    #         max_beauty = max(max_beauty, curr_beauty)
        
    #     return max_beauty

    
    # too much memory :(
    # def maximumBeauty(self, nums, k):
    #     n = len(nums)
    #     swap_map = defaultdict(list)
    #     for i in range(n):
    #         for j in range(nums[i] - k, nums[i] + k + 1):
    #             swap_map[i].append(j)
        
    #     value_count = defaultdict(int)
    #     for values in swap_map.values():
    #         for val in values:
    #             value_count[val] += 1
        
    #     return max(value_count.values())

nums = [4,6,1,2]
k = 2
sol = Solution()
print(sol.maximumBeauty(nums, k))
