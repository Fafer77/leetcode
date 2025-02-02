from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)

        # it keeps info whether substring s[i:j+1] is palidnrome or not
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res



# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         part = []

#         def dfs(i):
#             if i >= len(s):
#                 res.append(part.copy())
#                 return
#             for j in range(i, len(s)):
#                 if self.is_pali(s, i, j):
#                     part.append(s[i:j+1])
#                     dfs(j + 1)
#                     part.pop()
        
#         dfs(0)
#         return res
    
#     def is_pali(self, s, l, r):
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l, r = l + 1, r - 1
#         return True