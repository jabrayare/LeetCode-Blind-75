from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        result = []
        
        
        while len(lists) > 1:
            mergeLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                # Merge the two lists and add it to your mergelists List
                mergeLists.append(self.mergeTwoLists(l1, l2))
            lists = mergeLists
        return lists[0]
            
            
            
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