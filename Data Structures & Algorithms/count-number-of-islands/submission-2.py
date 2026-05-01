class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    numIslands += 1
                queue = [(i,j)]
                while queue:
                    x, y = queue.pop()
                    if x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0 and grid[x][y] == "1" and (x, y) not in visited:
                        queue.append((x, y + 1))
                        queue.append((x + 1, y))
                        queue.append((x - 1, y ))
                        queue.append((x, y - 1))
                    visited.add((x, y))

        return numIslands




        