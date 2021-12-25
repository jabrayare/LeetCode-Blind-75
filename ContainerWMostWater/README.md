## Problem: https://leetcode.com/problems/container-with-most-water/

## Solutions Idea

> Use a sliding window technique with two pointers.

- Left pointer starting from the beggining of the array.
- Right pointer starting from the end of the array.
- Calculate the area of the window by multiplying the min(array[left], array[right]) and the length of the window by finding the abs(right-left)
- Increment left pointer of the array[left] is less than the array[right].
- otherwise decrement right pointer.
- Keep truck of the largest area in each iteration.
- return the largest area.
