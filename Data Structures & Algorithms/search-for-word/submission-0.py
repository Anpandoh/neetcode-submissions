class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y , width, height, curr, visited):
            if x >= 0 and x < width and  y >= 0 and y < height and board[x][y] == word[curr] and (x,y) not in visited:
                if curr == len(word) - 1:
                    return True
                visited.add((x,y))
                if dfs(x, y + 1, width, height, curr + 1, visited) or dfs(x, y - 1, width, height, curr + 1, visited) or dfs(x + 1, y, width, height, curr + 1, visited) or dfs(x - 1, y, width, height, curr + 1, visited):
                    return True
                visited.remove((x,y))
                return False
            else:
                return False
            





        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i,j,m,n, 0, visited):
                        return True
        return False

        

        