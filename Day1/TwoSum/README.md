> > Problem: https://leetcode.com/problems/two-sum/

### Solution Ideas.

> Brute Force.

- Use two for loops to find two numbers that add up to the target.

> Optimized solution.

- Use a dictionary/hashmap to keep track of difference between the target and the current number in the for loop.
- Add the current number in the map with its current index
  - if its difference is not in the map.
  - otherwise return the current index and the previous index that is in the map.
