class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s = set(nums) 
        d = {i: 0 for i in s}
        k = len(nums)//3
        for i in range(len(nums)):
            if nums[i] in list(d.keys()):
                d[nums[i]] += 1
        result = [key for key, val in d.items() if val > k]
        return result