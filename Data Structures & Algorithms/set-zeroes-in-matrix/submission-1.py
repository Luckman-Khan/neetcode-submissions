class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS,COLS = len(matrix), len(matrix[0])
        rows,cols = [False]*ROWS,[False]*COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for r in range(ROWS):
            for c in range(COLS):

                if rows[r] or cols[c]:
                    matrix[r][c] = 0
        
            
