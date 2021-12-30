## Problem: `https://leetcode.com/problems/group-anagrams/`

### Solution Idea

> Use a dictionary to keep track of words.

- Loop through the words in the array,
- Use a dictionary with the key: sorted word and the value: an array of all the words that map to that sorted word.
- At end return the values of the dictionary.

- You can use a regular dictionary/map in python or defaultdict.
