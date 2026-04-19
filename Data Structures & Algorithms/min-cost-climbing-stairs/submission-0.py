class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        d = [0] * n
        d[0] , d[1] = cost[0], cost[1]
        for i in range(2, n):
            d[i] = cost[i] + min(d[i-1], d[i-2])
        return min(d[n-1], d[n-2])
        