class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(path, nums):
            if not nums:
                result.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, nums[:i]+ nums[i+1:])
                path.pop()
        backtrack([], nums)
        return result