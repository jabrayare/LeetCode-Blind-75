## Problem: `https://leetcode.com/problems/3sum/`

### Solution Idea

> Using a two pointer inside a for loop.

- Use a for loop and in each iteration find two numbers that come after the current number that if you add all of them will give you `0`.
- Using two pointer will help you find those two numbers.
- `left` pointer start current `index + 1`
- `Right` pointer start `len(nums)-1`
- if adding all of numbers give you `0`, then add it to your result array.
- if the numbers are less than `0`, then increment `left` pointer
- otherwise decrement `right` pointer.
- At the end, return result
