class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums) 
        d = {i: 0 for i in s}
        for i in range(len(nums)):
            if nums[i] in list(d.keys()):
                d[nums[i]] += 1
        return max(d, key = d.get)
        