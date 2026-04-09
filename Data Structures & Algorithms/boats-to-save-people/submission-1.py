class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l = 0
        h = len(people)-1
        while l <= h:
            if people[l] + people[h] <= limit :
                l += 1
            h -= 1
            count += 1
        return count