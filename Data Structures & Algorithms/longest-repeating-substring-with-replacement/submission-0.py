class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} ## dictionary with 26 upper case letters
        l = 0 ## left pointer for the sliding window
        maxf = 0 ## max frequency to track how many times a letter pops up
        result = 0 ## we intialize the 3 things that can change

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1


            maxf = max(maxf, count[s[r]])


            if (r - l + 1) - maxf > k:

                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result
