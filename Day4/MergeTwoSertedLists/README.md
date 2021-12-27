## Problem: `https://leetcode.com/problems/merge-two-sorted-lists/`

### Solution Idea.

> Using a dummy_head to keep reference to the head of linkedList.

- Loop through both list as long as both of them are not null.

  - If list1.val < list2.val,
    - Add list1 to your result linkedList and move list1 pointer and result pointer.
    - Otherwise add list2 to your result linkedList and move list2 pointer and result pointer.

- If list1 is null, add it to your result linkedlist and move result pointer.
- Otherwise, add list2 to your result linkedlist and move result pointer.
- At the end, `return dummy_head.next`
