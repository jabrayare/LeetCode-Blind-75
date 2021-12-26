## Problem: `https://leetcode.com/problems/remove-nth-node-from-end-of-list/`

### Solution Ideas

> Multiple passes.

- Make one pass to the linkedlist to get the length.
- Substract the length of LL from the given n.
- Move your current pointer as long as `length >= 0` and curr pointer is not null.
- When the length hits `0`, you know you're at the point where you need to remove the node. `curr.next = curr.next.next`
- Return `dummy_head.next`

> Use a slow and fast pointer.

- Move your fast pointer as long as the give n is greater than `0`.
- Move your fast and slow pointer as long as the fast pointer is not null(NONE)
- When the fast pointer hits null/None, you know you are the point where you need to remove the node. `slow.next = slow.next.next`
- Return `dummy_head.next`

> In both of the solutions we're using a dummy_head to keep the reference to the head.
