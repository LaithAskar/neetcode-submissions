class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Sum of every integer from 0 through n
        expected_sum = n * (n + 1) // 2

        # Sum of the numbers that are actually present
        actual_sum = sum(nums)

        return expected_sum - actual_sum
        