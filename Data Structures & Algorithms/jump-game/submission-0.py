class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Farthest index reachable so far
        farthest = 0

        for i in range(len(nums)):
            # If the current index cannot be reached
            if i > farthest:
                return False

            # Update using the destination reachable from index i
            farthest = max(farthest, i + nums[i])

            # Optional early success
            if farthest >= len(nums) - 1:
                return True

        return True
