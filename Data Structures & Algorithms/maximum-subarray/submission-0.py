class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Both begin with the first element
        current_sum = nums[0]
        best_sum = nums[0]

        # Process every element after the first
        for x in nums[1:]:
            # Choose: start at x, or extend the previous subarray
            current_sum = max(x, current_sum + x)

            # Update the best sum found anywhere
            best_sum = max(best_sum, current_sum)

        return best_sum
