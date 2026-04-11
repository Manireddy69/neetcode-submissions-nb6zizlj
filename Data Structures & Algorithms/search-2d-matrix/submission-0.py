class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = m*n -1
        while l <= h:
            mid = (l+h)//2
            curr = matrix[mid//n][mid % n]
            if curr == target:
                return True
            elif curr < target:
                l = mid + 1
            else:
                h = mid -1
        return False