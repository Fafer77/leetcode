from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        if not shortest:
            return ""
        
        for i, letter in enumerate(shortest):
            for s in strs:
                if s[i] != letter:
                    return shortest[:i]

        return shortest
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
