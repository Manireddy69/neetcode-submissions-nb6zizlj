class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total //2
        d = {0}
        for stone in stones:
            new_d = set()
            for s in d:
                new_d.add(s + stone) # add the stone
                new_d.add(s)
            d = new_d
        best = max(s for s in d if s <= target)
        return total - 2 * best
    