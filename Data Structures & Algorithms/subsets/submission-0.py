class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, curr_sub):
            result.append(curr_sub.copy())
            for i in range(start, len(nums)):
                curr_sub.append(nums[i]) #take each element
                backtrack(i+1, curr_sub) # backtrack taking each subsets
                curr_sub.pop() # pop the last append element
        backtrack(0, [])
        return result
            