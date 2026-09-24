class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) ## so it doesnt go out of bounds

        prefix = 1 ## start the prefix at 1 because anything multiplies at 1 is 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, - 1, - 1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
 
        