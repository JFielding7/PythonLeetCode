# Definition for singly-linked list.
from math import gcd


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(0)
nodes = [head]

L = 212
S = 635
curr = head
for i in range(1, L + S):
    next = ListNode(i)
    nodes.append(next)
    curr.next = next
    curr = next
curr.next = nodes[S]

slow = head
fast = head.next
count = 1
while slow is not fast:
    # print(slow.val, fast.val)
    slow = slow.next
    fast = fast.next.next
    count += 1

l = 1
fast = fast.next
while slow is not fast:
    l += 1
    slow = slow.next
    fast = fast.next.next

print("Count:", count)
print("Loop len:", l)

