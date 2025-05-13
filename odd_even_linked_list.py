from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        evens_tail = head
        odds_head = head.next
        prev = odds_head
        curr = odds_head.next

        while curr:
            next = curr.next
            curr.next = odds_head
            prev.next = next
            evens_tail.next = curr
            if next is None:
                break
            evens_tail = curr
            prev = next
            curr = next.next

        return head

nodes = [1,2,3,4,5]
head = None
for n in reversed(nodes):
    head = ListNode(n, head)

head = Solution().oddEvenList(head)
while head:
    print(head.val)
    head = head.next
