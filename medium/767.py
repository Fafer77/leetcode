from collections import deque, Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_ = max(counter.values())
        if max_ > ((len(s) + 1) // 2):
            return ""
        
        result = ""
        time = 0
        q = deque()
        print(counter)
        max_heap = [(-val, letter) for letter, val in counter.items()]
        heapq.heapify(max_heap)

        while max_heap or q:
            time += 1
            
            if max_heap:
                val, letter = heapq.heappop(max_heap)
                result += letter
                if val < -1:
                    q.append((val + 1, letter, time + 1))

            if q and q[0][2] == time:
                heapq.heappush(max_heap, q.popleft()[:2])
        
        return result


sol = Solution()
print(sol.reorganizeString(""))

