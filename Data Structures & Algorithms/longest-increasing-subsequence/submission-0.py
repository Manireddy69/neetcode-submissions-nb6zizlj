class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        d = [1]* n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    d[i] = max(d[i], 1+ d[j])
        return max(d)