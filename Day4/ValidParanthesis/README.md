## Problem: `https://leetcode.com/problems/valid-parentheses/`

### Solution Idea.

> Using a stack to keep track of opening and closing paranthesis.

- Loop through your string
- if the current character is an open paranthesis
  - Add it to the stack.
- If its a closing paranthesis and there is a matching paranthesis on the top of the stack.
  - Remove it from the stack.
- If the stack is empty and the current character is a closing paranthesis,
  - Return False
- If the stack is not empty and the current character doesn't match the character on the top of the stack,

  - Return False

- At the end, `return len(stack) == 0`
