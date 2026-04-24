class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = [0] * (target+1)
        d[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    d[i] = d[i] + d[i-num]
        return d[target]