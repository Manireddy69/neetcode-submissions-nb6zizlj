class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) ==1:
            return nums[0]
        d = {0: nums[0],
            1 : max(nums[0],nums[1])}
        for i in range(2, len(nums)):
            d[i] = max(d[i-1], d[i-2]+ nums[i])
        return max(d.values())