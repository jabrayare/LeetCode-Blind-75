def isValid(s: str) -> bool: 
    stack = []
    for p in s:
      if p in ['(', '[', '{']:
          stack.append(p)
      elif len(stack) > 0 and p == ')' and stack[-1] == '(':
          stack.pop()
      elif len(stack) > 0 and p == ']' and stack[-1] == '[':
          stack.pop()
      elif len(stack) > 0 and p == '}' and stack[-1] == '{':
          stack.pop()
          
      elif len(stack) == 0 and p in [')', ']', '}' ]:
          return False
      elif len(stack) > 0 and p == ')' and stack[-1] != '(':
          return False
      elif len(stack) > 0 and p == ']' and stack[-1] != '[':
          return False
      elif len(stack) > 0 and p == '}' and stack[-1] != '{':
          return False
            
    return len(stack) == 0

s = "()[]{}"
# Output: true
print(isValid(s))