from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #Edge case for empty nodes
        if n == 0:
            return 0

        #create an adjacency list
        adj = [[] for _ in range(n)]
        visited = set()
        
        for v,e in edges:
            adj[v].append(e)
            adj[e].append(v)

       #variable for connected component
        res = 0

        def bfs(start_node):

            queue = deque([start_node])
            visited.add(start_node)

            while queue:
                curr = queue.popleft()

                for neighbour in adj[curr]:
                    
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                    else:
                        continue
        
        for i in range(n):
            if i not in visited:
                bfs((i))
                res += 1

        return res


        

