class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        best_length = 1
        
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > best_length:
                        best_start = l
                        best_length = r - l + 1
                    l -= 1
                    r += 1
        
        return s[best_start : best_start + best_length]