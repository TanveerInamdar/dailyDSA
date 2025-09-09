# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        dummy = head
        checker = head
        curr = dummy
        current = dummy

        while current and current.next:
            current = current.next
            current = current.next
            curr = curr.next

        mid = curr
        prev = None
        x = curr
        curr = curr.next

        while x:
            x.next = prev
            prev = x

            if curr:
                x = curr
                curr = curr.next
            else:
                break

        # if checker and x:
        #     return None

        while checker and x:
            if x.val != checker.val:
                return False
            x = x.next
            checker = checker.next
        return True
