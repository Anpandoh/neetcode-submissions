class Solution:

    def checkRule(self, startX, startY, rangeX, rangeY, board: List[List[str]], validSet: set()) -> bool:
        
        for row in range(0,rangeX):
            for col in range(0,rangeY):
                if board[startX + row][startY + col] != '.':
                    # print(startX + row, startY + col)
                    # print(board[startX + row][startY + col])
                    if int(board[startX + row][startY + col]) > 0 and int(board[startX + row][startY + col]) <= 9 and int(board[startX + row][startY + col]) not in validSet:
                        validSet.add(int(board[startX + row][startY + col]))
                    else:
                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0, 3):
            for j in range(0,3):
                validSet = set()
                if not self.checkRule(i * 3, j * 3, 3, 3, board, validSet):
                    return False

        for row in range(0,9):
            validSet = set()
            for col in range(0,9):
                if board[col][row] != '.':
                    if int(board[col][row]) > 0 and int(board[col][row]) <= 9 and int(board[col][row]) not in validSet:
                        validSet.add(int(board[col][row]))
                    else:
                        return False


        for row in range(0,9):
            validSet = set()
            for col in range(0,9):
                if board[row][col] != '.':
                    print(row, col, board[row][col])
                    if int(board[row][col]) > 0 and int(board[row][col]) <= 9 and int(board[row][col]) not in validSet:
                        validSet.add(int(board[row][col]))
                    else:
                        return False

        return True





                

        