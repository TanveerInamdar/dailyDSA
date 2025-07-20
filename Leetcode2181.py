# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        curr.next = head
        curr = curr.next
        prev = dummy
        prev.next = head
        count = 0
        while curr:
            if curr.val != 0:
                count += curr.val
                prev.next = curr
                curr = curr.next
            else:
                curr.val = count
                prev.next = curr
                count = 0
                prev = prev.next
                curr = curr.next
        return dummy.next.next