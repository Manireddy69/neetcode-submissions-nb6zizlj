class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, nums):
            if not nums:
                result.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path, nums[:i] + nums[i+1:])
                path.pop()
        backtrack([], nums)
        return result