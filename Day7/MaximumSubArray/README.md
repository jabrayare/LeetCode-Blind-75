## Problem: `https://leetcode.com/problems/maximum-subarray/`

### Solution Idea

> Keep track of current sum and max sum

- Loop through the elements,
  - If the current element is greater than the current max
    - Update your current max to the current element
  - Other wise add the current element to the current max
  - Update your max sum

* At the end, return the max sum

* Complexity:
  - Time complexity: O(N)
  - Space complexity: O(1)
