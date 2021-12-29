## Problem: `https://leetcode.com/problems/combination-sum/`

### Solution Idea

> Use Backtracking.

- Do a dfs on each element of the combination as long as we don't get out of bound or our total becomes greater than the target.
- If our dfs total gets equal to the target add the combination to our result array.
- At the end return result.
