from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        rows = [0] * m
        cols = [0] * n
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        res += 1

        return res

# alterantywna opcja -> zliczenie tych gdzie jest rows[i] = 1 and cols[i] = 1
# i odjecie od wszystkcih serwerow je

