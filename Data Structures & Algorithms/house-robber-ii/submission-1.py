class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house_1(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums)
            d = [0] * n
            d[0], d[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                d[i] = max(d[i-1], nums[i] + d[i-2])
            return d[-1]
        return max(house_1(nums[:-1]), house_1(nums[1:]))
