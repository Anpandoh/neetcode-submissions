class Solution:
    def solve(self, board: List[List[str]]) -> None:


        #go through the board and start bfs when an O is found and is not in visited set. Stop bfs if an edge is found and don't do anything afterwards. While doing bfs keep track of Os as part of visited set, if not X was found replace all the Os with Xs
        
        


        for i in range(len(board)):
            for j in range(len(board[0])):
                replaceOs = True
                if board[i][j] == "O":
                    q = [(i,j)]
                    visited = set()
                    while q:
                        currI, currJ = q.pop(0)
                        if currI >= len(board) or currI < 0 or currJ >= len(board[0]) or currJ < 0:
                            replaceOs = False
                            break
                        elif (currI, currJ) in visited:
                            continue
                        elif board[currI][currJ] == "O":
                            visited.add((currI, currJ))
                            q.append((currI + 1, currJ))
                            q.append((currI - 1, currJ))
                            q.append((currI, currJ + 1))
                            q.append((currI, currJ - 1))
                    if replaceOs:
                        for x, y in visited:
                            board[x][y] = "X"


                    