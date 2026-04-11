class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        result = x
        while l <= h:
            m = (l+h)//2
            if m*m <= x:
                result = m
                l = m + 1
            else:
                h = m -1
        return result

