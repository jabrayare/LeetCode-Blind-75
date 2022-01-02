## Problem: `https://leetcode.com/problems/climbing-stairs/`

### Solution Idea

> Dynamic programming.

- Initialize your dp array to zeroes \* n + 1
- Set the first two indexes to 1
- Loop through the array
- Assign each element of the array to the values of the previous two elements
- At the end return the last element of the array.
