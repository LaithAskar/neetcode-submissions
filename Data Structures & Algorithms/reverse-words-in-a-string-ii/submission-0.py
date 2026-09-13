class Solution:
    def reverseWords(self, s: List[str]) -> None:
        def reverse_range(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        reverse_range(s, 0, len(s) - 1)
        start = 0
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == ' ':
                reverse_range(s, start, end - 1)
                start = end + 1
        return