## Problem: `https://leetcode.com/problems/merge-intervals/`

### Solution Idea.

- Sort the intervals by their first value.
- Put the first interval in the result array.
- Loop through intervals starting from the second interval.
- Check if the previous interval and the current interval overlap.

  - You can check overlaps by checking if the previous interval end after the second interval starts.
  - If overlaps happen combine the two intervals.
  - Otherwise just add the interval to the result array, and update your previous interval with the current interval.

- At the end return the result array.

- Complexities

  - Time complexity - O(Nlog(N))
  - Space complexity - O(N)
