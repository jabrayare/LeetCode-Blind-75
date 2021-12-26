from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution1
        """
        dummy_head = ListNode(0, head)
        curr = head
        length = 0
        
        while curr and curr.next:
            length += 1
            curr = curr.next
        length -= n
        curr = dummy_head
        while length >= 0 and curr:
            curr = curr.next
            length -= 1
        curr.next = curr.next.next
        return dummy_head.next
        """
        # Solution#2
        # Slow and fast pointer.
        dummy_head = ListNode(0, head)
        fast = head
        slow = dummy_head
        
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return dummy_head.next