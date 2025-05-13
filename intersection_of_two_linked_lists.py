from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def len_and_tail(node):
    prev = None
    length = 0

    while node:
        prev = node
        node = node.next
        length += 1

    return length, prev

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        len_a, tail_a = len_and_tail(head_a)
        len_b, tail_b = len_and_tail(head_b)

        if tail_a != tail_b:
            return None

        curr_a = head_a
        for _ in range(len_a - len_b):
            curr_a = curr_a.next

        curr_b = head_b
        for _ in range(len_b - len_a):
            curr_b = curr_b.next

        while curr_a != curr_b:
            curr_a = curr_a.next
            curr_b = curr_b.next

        return curr_a
