from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return None

        #variables
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        edges = set()
        final_paths = []
        row = len(board)
        col = len(board[0])


        def bfs(start_node,graph):
            queue = deque([start_node])
            visited.add(start_node)
            current_path = []
            touches_edge = False

            while queue:
                curr = queue.popleft()
                current_path.append(curr)
                r,c = curr

                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
        
                    if (
                        0 <= nr < row and
                        0 <= nc < col and 
                        (nr,nc) not in visited and
                        graph[nr][nc] == "O"
                    ):
                        if (nr,nc) not in edges:
                            current_path.append((nr,nc))
                            visited.add((nr,nc))
                            queue.append((nr,nc))
                        else:
                            touches_edge = True
                            visited.add((nr,nc))

            if not touches_edge:
                for i,j in current_path:
                    board[i][j] = "X"
                        


                    
        for i in range(row):
            edges.add((i, 0))
            edges.add((i, col - 1))
            for j in range(col):
                edges.add((0, j))
                edges.add((row - 1, j))
                   

        for i in range(row):
            for j in range(col):
                if (
                    board[i][j] == "O" and 
                    (i,j) not in edges and
                    (i,j) not in visited
                ):
                    bfs((i,j),board)
                    

        