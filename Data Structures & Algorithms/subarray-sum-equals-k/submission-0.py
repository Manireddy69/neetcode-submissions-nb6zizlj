class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        hash_map = {0:1}
        for num in nums:
            curr += num
            if curr-k in hash_map:
                count += hash_map[curr - k]
            hash_map[curr] = hash_map.get(curr, 0) + 1
        return count