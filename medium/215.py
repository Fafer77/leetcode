from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[i])
                
        return min_heap[0]

# second solution

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        min_ = 0
        while k > 0:
            min_ = heapq.heappop(max_heap)
            k -= 1
        
        return -min_
