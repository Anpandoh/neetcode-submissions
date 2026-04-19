class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        x = 0
        y = 0
        maxX = len(matrix) - 1
        maxY = len(matrix[0]) - 1
        minX = 1
        minY = 0
        Xiterator = 0
        Yiterator = 1
        visited = set()
        res = []
        # if maxX  == 0 and maxY == 0 :
        #     return [matrix[0][0]]
        while (x, y) not in visited and x < len(matrix) and y < len(matrix[0]) and x >= 0 and y >= 0:
            visited.add((x,y))
            res.append(matrix[x][y])
            if x == maxX and Xiterator == 1:
                Xiterator = 0
                Yiterator = -1
                maxX -= 1
            elif x == minX and Xiterator == -1:
                Xiterator = 0
                Yiterator = 1
                minX += 1
            elif y == minY and Yiterator == -1:
                Xiterator = -1
                Yiterator = 0
                minY += 1
            elif y == maxY and Yiterator == 1:
                Xiterator = 1
                Yiterator = 0
                maxY -= 1

            x += Xiterator
            y += Yiterator
            print(x,y)
    
        return res


