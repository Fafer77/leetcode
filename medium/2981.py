from collections import defaultdict

class Solution:
    # O(n^2)
    def maximumLength(self, s):
        substring_counter = defaultdict(int)
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring_counter[s[i:(j + 1)]] += 1

        max_len = 0
        for substring, counter in substring_counter.items():
            if len(set(substring)) == 1 and counter >= 3 and len(substring) > max_len:
                max_len = len(substring)

        if max_len:
            return max_len
        else:
            return -1

    # O(n)
    def maxLength(self, s):
        max_len = -1
        n = len(s)
        
        i = 0
        while i < n:
            char = s[i]
            count = 0
            
            while i < n and s[i] == char:
                count += 1
                i += 1
            
            if count >= 3:
                max_len = max(max_len, count)
        
        return max_len


sol = Solution()
print(sol.maximumLength('"abcaba"'))
