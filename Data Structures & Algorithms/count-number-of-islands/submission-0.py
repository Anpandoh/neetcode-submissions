class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        visited = set()
        numIslands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    queue = []
                    queue.append((i,j))
                    while queue:
                        currX, currY = queue.pop(0)
                        print(currX, currY)
                        if currX < m and currX >= 0 and currY < n and currY >= 0 and (currX,currY) not in visited and grid[currX][currY] == "1":
                            queue.append((currX, currY + 1))
                            queue.append((currX, currY - 1))
                            queue.append((currX + 1, currY))
                            queue.append((currX - 1, currY))
                            visited.add((currX,currY))
                    numIslands += 1

        return numIslands                      
