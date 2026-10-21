class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def backtrack(row,col,index,path): 

            if row < 0 or row >= len(board):
                return False
            
            if col < 0 or col >= len(board[0]):
                return False
            
            if board[row][col] != word[index]:
                return False
            
            if (row,col) in path:
                return False
            
            if index == len(word) - 1:
                return True

            path.add((row, col))

            found = (
                backtrack(row - 1, col, index + 1, path) or
                backtrack(row + 1, col, index + 1, path) or
                backtrack(row, col + 1, index + 1, path) or
                backtrack(row, col - 1, index + 1, path)
            )

            path.remove((row, col))

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0, path):
                    return True

        return False

