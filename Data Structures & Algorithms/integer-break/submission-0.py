class Solution:
    def integerBreak(self, n: int) -> int:
        d = {1: 1}
        def dfs(num):
            if num in d:
                return d[num]
            d[num] = 0 if num == n else num
            for i in range(1,num):
                val = dfs(i) * dfs(num-i)
                d[num] = max(d[num], val)
            return d[num]
        return dfs(n)