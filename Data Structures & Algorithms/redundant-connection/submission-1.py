from collections import deque, defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #Edge case for empty edges list
        if not edges:
            return []

        
        #Adjacency list
        adj = defaultdict(list)


        for v,e in edges:
            visited = set()

        
            queue = deque([v])
            visited.add(v)

            while queue:
                curr = queue.popleft()

                for neighbour in adj[curr]:
                    
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                    else: 
                        continue

            if e in visited:
                return [v,e]

            adj[v].append(e)
            adj[e].append(v)



        