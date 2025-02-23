from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort() # O(nlogn)
        intersection_x_s = points[0][0]
        intersection_x_e = points[0][1]
        sep_intersections = 1
        # O(n)
        for i in range(1, len(points)):
            guard = False
            candidate_x_s = points[i][0]
            candidate_x_e = points[i][1]
            if candidate_x_s >= intersection_x_s and candidate_x_s <= intersection_x_e:
                intersection_x_s = candidate_x_s
                guard = True
            if candidate_x_e >= intersection_x_s and candidate_x_e <= intersection_x_e:
                intersection_x_e = candidate_x_e
                guard = True
            if not guard:
                sep_intersections += 1
                intersection_x_s = candidate_x_s
                intersection_x_e = candidate_x_e
                
        return sep_intersections
    

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        answer = 1
        end = points[0][1]
        for s, e in points:
            if s > end:
                answer += 1
                end = e
            elif e < end:
                end = e
        
        return answer



