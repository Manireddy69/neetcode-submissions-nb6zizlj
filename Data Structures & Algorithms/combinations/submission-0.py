class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:return [list(range(1, n+1))]
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        backtrack(1, [])
        return result