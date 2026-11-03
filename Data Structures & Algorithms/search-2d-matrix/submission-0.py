class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            first_element = matrix[i][0]
            last_element = matrix[i][col - 1]
            if first_element <= target <= last_element:
                for j in range(col):
                    if matrix[i][j] == target:
                        return True
            
                


        return False
