class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    #set whole row to 'T' besides 0
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = pow(2, 31)
                    #set whole col to 'T'
                    for l in range(m):
                        if matrix[l][j] != 0:
                            matrix[l][j] = pow(2, 31)


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == pow(2, 31):
                    matrix[i][j] = 0
        


        
        