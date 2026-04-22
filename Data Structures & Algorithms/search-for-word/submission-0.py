class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        def backtrack(r, c, remaining):
            if not remaining:
                return True
            if (r < 0 or r >= row or 
            c < 0 or c >= col or board[r][c] != remaining[0]):
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = (backtrack(r+1, c, remaining[1:])or
            backtrack(r-1, c, remaining[1:])or 
            backtrack(r, c+1, remaining[1:])or
            backtrack(r, c-1, remaining[1:]))
            board[r][c] = temp
            return found
        for r in range(row):
            for c in range(col):
                if backtrack(r, c,word):
                    return True
        return False