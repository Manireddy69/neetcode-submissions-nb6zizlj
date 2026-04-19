class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1,2
        count = 2
        while count < n:
            a, b = b, a+b
            count += 1
        return b