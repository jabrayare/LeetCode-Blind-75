Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Solution Ideas.

> > Sliding Window Technique.

- Loop over the elements.
- if the current element is not in the window
  - Add it to the window(Expand the window)
- Else
  - Remove it from the window(Shrink the window)
- Calcualte the largest window by always keeping the track of the size of the window in each iteration.

> > Time complexity - O(N) - Where n is the number of chars in the given string.
> > Space complexity - O(N) - where n is the number of elements we store in the window.
