class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row: int, col: int, i: int, board: List[List[str]]):
            if (row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == "#" or board[row][col] != word[i]):
                return False
            if board[row][col] == word[i]:
                if i == len(word) - 1:
                    return True
                else:
                    board[row][col] = "#"
                    res = (dfs(row - 1, col, i+1, board) or
                           dfs(row + 1, col, i+1, board) or
                           dfs(row, col - 1, i+1, board) or
                           dfs(row, col + 1, i+1, board))
                    board[row][col] = word[i]
                    return res

        rows = len(board)
        cols = len(board[0])
        for row in range(0, rows):
            for col in range(0, cols):
                if dfs(row, col, 0, board):
                    return True
        return False