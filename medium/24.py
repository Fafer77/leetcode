from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            prev = curr.next
            new = curr.next.next

            prev.next = new.next
            new.next = prev
            curr.next = new

            curr = curr.next.next
    
        return dummy.next


sol = Solution()
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
sol.swapPairs(node1)
