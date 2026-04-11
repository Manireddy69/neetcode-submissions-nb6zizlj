class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## DP
        d = [0] * len(nums)
        d[0] = nums[0]
        for i in range(1, len(nums)):
            d[i] = max(nums[i], nums[i] + d[i-1])
        return max(d)