## Problem: `https://leetcode.com/problems/search-in-rotated-sorted-array/`

## Solution Ideas.

> Linear Search

- Loop through the array and check if the current element is equal to the target, if it does, then return the index.
- At the end, return -1
  - Time complexity - O(N)
  - Space complexity - O(1)

> Binary Search

- use two pointers low and high,
- Loop as long as `low <= high`
- If the target is equal to the element at mid.
  - `return mid`
- If the element at low is less than or equal to the element at mid

  - Then you need to search in the left sorted portion of the array.

  - if the target is greater than the mid element or its less than the low element, then set your `low = mid + 1`
  - Otherwise set your `high = mid - 1`

- Other wise, you neeed to search in the right sorted portion of the array.

  - if the target is less than the mid element or its greater then the high element, then set your `high = mid - 1`
  - Otherwise set your `low = mid + 1`

- At the end, `return - 1`

  - Time complexity - O(log(n))
  - Space complexity - O(1)
