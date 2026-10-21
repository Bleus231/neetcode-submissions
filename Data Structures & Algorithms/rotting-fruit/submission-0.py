from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #Empty edge case
        if not grid:
            return -1

        
        #Variables

        #Directions ~ adjacent
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        visited = set()
        current_time = 0
        fresh_oranges = 0


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                
                if grid[i][j] == 1:
                    fresh_oranges += 1

        
        while queue and fresh_oranges != 0:    

            layer_size = len(queue)
            for _ in range(layer_size):
                curr = queue.popleft()
                r,c = curr
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc

                    #condition check in bound
                    if(
                        0 <= nr < row and
                        0 <= nc < col and 
                        (nr,nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        visited.add((nr,nc))
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh_oranges -= 1
            current_time += 1

        if fresh_oranges > 0:
            return -1
        else:
            return current_time

            

                             
