class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums) 
        d = {i: 0 for i in s}
        for i in range(len(nums)):
            if nums[i] in list(d.keys()):
                d[nums[i]] += 1
        sorted_keys = sorted(d, key=d.get, reverse=True)
        result = sorted_keys[:k]
        return result