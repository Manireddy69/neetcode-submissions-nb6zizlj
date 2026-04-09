class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = list(sorted(set(nums)))
        l = len(s)
        result = 1
        current = 1   
        if len(nums) == 0:
            return 0      
        for i in range(1,l):
            if s[i] == s[i-1] +1:
                current += 1   
                result = max(result, current)  
            else:
                current = 1      
        return result