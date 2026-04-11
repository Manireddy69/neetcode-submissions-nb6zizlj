class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = sum(weights)
        result = h
        while l <= h:
            mid = (l+h)//2
            d = 1
            s = 0
            for num in weights:
                s += num
                if s > mid:
                    d += 1 ## new day
                    s = num
            if d <= days:
                result = mid 
                h = mid -1
            else:
                l = mid +1 
        return result