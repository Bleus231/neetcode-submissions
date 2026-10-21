from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        # Step 1: Find all treasure chests (0) and add them to the queue simultaneously
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # Directions for moving Up, Down, Left, Right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 2: Run Multi-Source BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and ensure the cell is an unvisited land cell (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    # Update distance layer-by-layer
                    grid[nr][nc] = grid[r][c] + 1
                    # Push to queue to continue the wave propagation
                    queue.append((nr, nc))