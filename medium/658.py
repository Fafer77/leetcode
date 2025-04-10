# max heap because I want to have easy access to element which has the biggest difference
# so that I can replace it easily

from typing import List
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k >= n:
            return arr

        max_heap = []
        for i in range(k):
            diff = abs(arr[i] - x)
            heapq.heappush(max_heap, (-diff, arr[i]))

        for i in range(k, n):
            diff = abs(arr[i] - x)
            curr_max_diff, num = max_heap[0]
            if diff < -curr_max_diff:
                heapq.heapreplace(max_heap, (-diff, arr[i]))
        
        result = []
        while max_heap:
            result.append(heapq.heappop(max_heap)[1])
        
        result.sort()
        return result



arr = [1,1,1,10,10,10]
k = 1
x = 9
sol = Solution()
sol.findClosestElements(arr, k, x)

