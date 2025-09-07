# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        current = l2
        adder = 0
        tail = ListNode(0)
        dummy = tail
        while curr or current or adder:
            i = curr.val if curr else 0
            j = current.val if current else 0
            x = i + j + adder
            adder = x // 10
            new = ListNode(x % 10)
            tail.next = new
            tail = tail.next
            if curr:
                curr = curr.next
            if current:
                current = current.next

        return dummy.next

