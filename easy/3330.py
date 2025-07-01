from collections import defaultdict

class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        n = len(word)
        curr_block_len = 1
        for i in range(1, n):
            if word[i-1] == word[i]:
                curr_block_len += 1
            else:
                count += curr_block_len - 1
                curr_block_len = 1

        return count + curr_block_len - 1
