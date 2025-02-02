from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.isPrefixandSuffix(words[i], words[j]):
                    count += 1
        return count
    

    def isPrefixandSuffix(self, str1: str, str2: str) -> False:
        l1 = len(str1)
        l2 = len(str2)
        if l1 > l2:
            return False
        elif l1 == l2:
            return str1 == str2
        
        prefix = str2[:l1]
        suffix = str2[-l1:]

        return prefix == str1 and suffix == str1


sol = Solution()
words = ["pa","papa","ma","mama"]
print(sol.countPrefixSuffixPairs(words))
