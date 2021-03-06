from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        result = dummy_head
        
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                result.next = list2
                result = result.next
                list2 = list2.next

        if list1:
            result.next = list1
            result = result.next
        else:
            result.next = list2
            result = result.next
        return dummy_head.next