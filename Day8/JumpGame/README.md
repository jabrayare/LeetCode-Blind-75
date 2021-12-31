## Problem: `https://leetcode.com/problems/jump-game/`

### Solution Idea

> Greedy Algorithm

- Start from the end(goal) going the first index.
- Update your goal with current index if the `current index + current element` is greater then the goal

- At the end of the loop, if goal is at index `0`, that means we can reach the last index from the first index otherwise we can't.
