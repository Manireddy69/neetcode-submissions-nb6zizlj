class Solution:
    def numSquares(self, n: int) -> int:
        d = [float('inf')] * (n+1)
        d[0] = 0
        i = 1
        s = []
        while i * i <= n:
            s.append(i*i)
            i += 1
        for i in range(1, n+1):
            for j in s:
                if j > i:
                    break
                d[i] = min(d[i] , 1+ d[i-j])
        return d[n]