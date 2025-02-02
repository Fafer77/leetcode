from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        len_pref = len(pref)
        for word in words:
            if len_pref <= len(word) and word[:len_pref] == pref:
                count += 1
        return count


sol = Solution()
print(sol.prefixCount(["pay","attention","practice","attend"], 'at'))
