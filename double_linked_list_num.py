from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rev(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = None
        curr = self.rev(head)

        while curr:
            curr_sum = (curr.val << 1) + carry
            res = ListNode(curr_sum % 10, res)
            carry = curr_sum // 10
            curr = curr.next
        if carry:
            res = ListNode(1, res)

        return res

num = ListNode(1, ListNode(8, ListNode(9)))
head = Solution().doubleIt(num)
while head:
    print(head.val)
    head = head.next