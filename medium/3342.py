from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0

        heap = [(0, 0, 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, x, y, parity = heapq.heappop(heap)
            if time > dist[x][y][parity]:
                continue

            if (x, y) == (n - 1, m - 1):
                return time

            cost = 1 if parity == 0 else 2
            new_parity = 1 - parity

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m:
                    new_time = max(time, moveTime[nx][ny]) + cost
                    if new_time < dist[nx][ny][new_parity]:
                        dist[nx][ny][new_parity] = new_time
                        heapq.heappush(heap, (new_time, nx, ny, new_parity))
        
        return -1

