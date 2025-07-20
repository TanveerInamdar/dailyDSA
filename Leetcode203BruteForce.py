class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head

        prev = dummy
        prev.next = curr
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next

            else:
                curr = curr.next
                prev = prev.next
        return dummy.next