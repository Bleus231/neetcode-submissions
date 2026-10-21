from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        island_count = 0
        visited = set()

        def bfs(start_node):
            queue = deque([start_node])
            visited.add(start_node)

            while queue:
                curr = queue.popleft()
                r, c = curr

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check grid boundaries, land value, and visited status
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] == "1" and 
                        (nr, nc) not in visited):
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # Scan every cell in the 2D grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs((i, j))
                    island_count += 1

        return island_count