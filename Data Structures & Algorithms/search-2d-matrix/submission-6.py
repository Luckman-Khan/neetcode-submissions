class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
    
        Top,Bot = 0,len(matrix)-1

        while Top<=Bot:
            row = (Top+Bot)//2

            if target>matrix[row][-1]:
                Top = row+1
            elif target<matrix[row][0]:
                Bot = row-1
            else:
                break
        
        if not Top<=Bot:
            return False
        

        row = (Top+Bot)//2
        left,right = 0, len(matrix[0])-1

        while left<=right:

            mid = (left+right)//2

            if target>matrix[row][mid]:
                left = mid+1
            elif target<matrix[row][mid]:
                right = mid-1
            else:
                return True
        
        return False

