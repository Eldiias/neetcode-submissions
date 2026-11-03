# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l1 = 0
        l2 = 0
        if not head: return False
        if not head.next:
            return False
        l1 = head
        l2 = head.next
        if l2.next is None:
            return False
        if l2.next.next is None:
            return False
        while l2 is not None:
            print(l1.val, l2.val)
            if l1==l2:
                return True
            else:
                l1 = l1.next
                l2 = l2.next.next if l2.next is not None and l2.next.next is not None else None
        return False
            