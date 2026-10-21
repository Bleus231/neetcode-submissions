from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        row, col = len(heights), len(heights[0])
        
        visited_pacific = set()
        visited_atlantic = set()
        
        # Reusable BFS function for going "upstream" (uphill)
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited:
                        # Reverse logic: can only flow inward if neighbor is >= current height
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
        
        # 1. Pacific Ocean Setup (Left column and Top row)
        pacific_queue = deque()
        for i in range(row):
            pacific_queue.append((i, 0))
            visited_pacific.add((i, 0))
        for j in range(col):
            pacific_queue.append((0, j))
            visited_pacific.add((0, j))
            
        bfs(pacific_queue, visited_pacific)
        
        # 2. Atlantic Ocean Setup (Right column and Bottom row)
        atlantic_queue = deque()
        for i in range(row):
            atlantic_queue.append((i, col - 1))
            visited_atlantic.add((i, col - 1))
        for j in range(col):
            atlantic_queue.append((row - 1, j))
            visited_atlantic.add((row - 1, j))
            
        bfs(atlantic_queue, visited_atlantic)
        
        # 3. Find the intersection of both oceans
        res = []
        for i in range(row):
            for j in range(col):
                if (i, j) in visited_pacific and (i, j) in visited_atlantic:
                    res.append([i, j])
                    
        return res