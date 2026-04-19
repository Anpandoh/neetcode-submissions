class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        r = len(heights)
        c = len(heights[0])
        res = []
        atlantic = set()
        pacific = set()

        def dfs(x, y, currList, prev):

            if (x,y) in currList or x >= r or y >= c or x < 0 or y < 0 or heights[x][y] < prev:
                return
            currList.add((x,y))
            dfs(x + 1, y, currList, heights[x][y])
            dfs(x - 1, y, currList, heights[x][y])
            dfs(x, y + 1, currList, heights[x][y])
            dfs(x, y - 1, currList, heights[x][y])
        


        for i in range(r):
            dfs(i , 0, pacific, heights[i][0])
            dfs(i , c - 1, atlantic, heights[i][c-1])
        
        for j in range(c):
            dfs(0 , j, pacific, heights[0][j])
            dfs(r - 1, j, atlantic, heights[r-1][j])
        
        # print(atlantic)
        res = []
        for a in range(r):
            for b in range(c):
                if (a , b) in atlantic and (a, b) in pacific:
                    res.append([a,b])

        

        return res
        




        