from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for passenger in details:
            age = int(passenger[11:13])
            if age > 60:
                counter += 1
            
        return counter