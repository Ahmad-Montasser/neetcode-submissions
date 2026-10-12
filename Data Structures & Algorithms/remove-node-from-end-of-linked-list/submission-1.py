# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        
        curr = head
        prev = None
        length = 0
        while curr:
            length += 1
            curr= curr.next
        curr = head
        if length-n == 0:
            return head.next
        
        for _ in range(length-n):
            prev = curr
            curr= curr.next
        if prev :
            prev.next = curr.next
        else:
            return None
        return head
        