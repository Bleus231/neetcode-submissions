from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        #Edge case where grid is empty
        if not grid:
            return 0
        
        #Up down left right for neighbours in BFS
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        max_area = 0 
        #Set to track visited nodes
        visited = set() 

        rows = len(grid)
        cols = len(grid[0])

        #BFS search
        def bfs(start_node,graph):
            queue = deque([start_node])
            visited.add(start_node)
            curr_area = 1 
            while queue:
                curr = queue.popleft()
                r,c = curr
                
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        curr_area += 1

            return curr_area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area,bfs((i, j),grid))
                    

        return max_area