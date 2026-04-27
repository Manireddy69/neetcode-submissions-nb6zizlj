class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # assign + to some numbers → call them group P
        # assign - to rest         → call them group N

        # P - N = target   ... (1)
        # P + N = total    ... (2)

        # add both:
        # 2P = target + total
        # P  = (target + total) / 2
        total = sum(nums)
        if abs(target) > total: ## if we can't reach target
            return 0
        if (target + total) % 2 != 0: ## correctness
            return 0
        p = (target + total)//2
        d = [0] * (p+1)
        d[0] = 1
        for num in nums:
            for i in range(p, num-1, -1):
                d[i] += d[i-num]
        return d[p]