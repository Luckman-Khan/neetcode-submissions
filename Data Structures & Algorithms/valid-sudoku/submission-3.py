class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = set()

            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                if val in seen:
                    return False
            
                seen.add(val)
        

        for i in range(9):
            seen = set()

            for j in range(9):
                val = board[j][i]

                if val == '.':
                    continue

                if val in seen:
                    return False
                
                seen.add(val)

        for row_number in range(0,9,3):

            for column_number in range(0,9,3):

                seen = set()
                for i in range(3):
                    for j in range(3):

                        val = board[row_number+i][column_number+j]
                        if val== '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True

