class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        d= {0}
        total = sum(stones)
        target = total //2

        for stone in stones:
            d = { s + stone for s in d} | d
        best = max(s for s in d if s <= target)
        return total - 2 * best
    