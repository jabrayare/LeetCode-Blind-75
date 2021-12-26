def longestPalindrome(s: str) -> str:
        res = ""
        longest = 0  
        for i in range(len(s)):
            # odd length
            left, right = i, i 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left: right + 1]
                left -= 1
                right += 1
            
            # Even length
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left: right + 1]
                left -= 1
                right += 1
        return res

s = "babad"
# Output: "bab"
print(longestPalindrome(s))