class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # try to find solution from every starting cell
        def dfs(r, c, i):
            if i == len(word): # i == current lent of matching path found
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False   # out of bounds or letter doesnt match word or visited already
            board[r][c] = '#' # mark visited
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))  # continue dfs with neighbours
            board[r][c] = word[i] # restore board for other paths to use
            return res

        # check if any True = word found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False