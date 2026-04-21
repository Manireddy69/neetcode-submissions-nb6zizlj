class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start, path, curr_sum):
            if curr_sum == target:
                result.append(path[:])
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, curr_sum + candidates[i])
                path.pop()
        backtrack(0,[], 0)
        return result                
