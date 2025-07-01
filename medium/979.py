from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(v):
            # leaf
            if v.left == None and v.right == None:
                balance = v.val - 1
                self.moves += abs(balance)
                return balance
            
            # not leaf
            if v.left != None:
                left_balance = dfs(v.left)
            else:
                left_balance = 0
            
            if v.right != None:
                right_balance = dfs(v.right)
            else:
                right_balance = 0
            
            balance = v.val + right_balance + left_balance - 1
            self.moves += abs(balance)

            return balance
        
        dfs(root)
        return self.moves

