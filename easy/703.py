from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, num)
            else:
                if num > self.min_heap[0]:
                    heapq.heapreplace(self.min_heap, num)

    def add(self, val: int) -> int:
        n = len(self.min_heap)
        if n < self.k:
            heapq.heappush(self.min_heap, val)
            return self.min_heap[0]
        
        if self.min_heap[0] < val:
            heapq.heapreplace(self.min_heap, val)
        
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)