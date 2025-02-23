from typing import List
from collections import defaultdict, Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_intervals = 0
        tasks_freq = defaultdict(int)
        for task in tasks:
            tasks_freq[task] += 1
        
        max_value = max(tasks_freq.values())
        sum_ = sum(1 for value in tasks_freq.values() if value == max_value)

        block_formula = (max_value - 1) * (n + 1) + sum_
        total_tasks = len(tasks)

        return max(total_tasks, block_formula)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        q = deque()
        time = 0
        max_heap = [-val for val in counter.values()]
        heapq.heapify(max_heap)

        while max_heap or q:
            time += 1

            if max_heap:
                val = 1 + heapq.heappop(max_heap)
                if val:
                    q.append((val, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time
