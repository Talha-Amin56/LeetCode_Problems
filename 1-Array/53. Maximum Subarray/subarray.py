class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = 0
        l = 0 
        max_sum = max(nums) 
        for r in range(len(nums)):
            acc = max(acc, 0)
            acc += nums[r]
            max_sum = max(max_sum,acc)
        return max_sum