# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        curr.next = head
        current = curr
        count = 0
        while count <= n:
            curr = curr.next
            count += 1
        while curr:
            curr = curr.next
            current = current.next
        current.next = current.next.next

        return dummy.next
