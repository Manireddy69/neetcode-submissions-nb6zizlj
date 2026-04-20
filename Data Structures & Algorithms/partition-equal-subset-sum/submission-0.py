class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # num = 1:  dp = [T, T, F, F, F, F, F, F, F, F, F, F]
        # num = 5:  dp = [T, T, F, F, F, T, T, F, F, F, F, F]
        # num = 11: dp = [T, T, F, F, F, T, T, F, F, F, F, T]  # 11 is reachable
        # num = 5:  dp = [T, T, F, F, F, T, T, F, F, F, T, T]  # 11 stays reachable
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        d= [False] * (target + 1)
        d[0] = True
        for num in nums:
            for j in range(target,num-1, -1):
                d[j] = d[j] or d[j-num]
        return d[target]