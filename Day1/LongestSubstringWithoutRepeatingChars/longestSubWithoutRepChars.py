def lengthOfLongestSubstring(s: str) -> int:
  # use a sliding window technique.
    largest = 0
    window = []
    first = 0
    second = 0
    
    while first < len(s) and second < len(s):
        if s[second] not in window:
            window.append(s[second])
            second += 1
        else:
            window.pop(0)
            first += 1
        largest = max(largest, len(window))
    
    return largest 

s = "abcabcbb"
# Output: 3
print(lengthOfLongestSubstring(s))