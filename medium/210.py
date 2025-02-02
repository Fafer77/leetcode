from typing import List
from collections import defaultdict

class Solution:
    def toposort(self, v, adj_list, stack, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for u in adj_list[v]:
            if not visited[u]:
                if self.toposort(u, adj_list, stack, visited, rec_stack):
                    return True
            elif rec_stack[u]:
                return True

        rec_stack[v] = False
        stack.append(v)
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        visited = [False] * numCourses
        rec_stack = [False] * numCourses
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[v].append(u)

        for v in range(numCourses):
            if not visited[v]:
                if self.toposort(v, adj_list, stack, visited, rec_stack):
                    return []

        stack.reverse()
        return stack

sol = Solution()
print(sol.findOrder(2, [[1,0],[0,1]]))
