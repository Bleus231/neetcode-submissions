
        
from collections import deque, defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Optimization: A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        
        # Step 2: Initialize BFS queue with (current_node, parent_node)
        # We use -1 as the parent for the starting root node (0)
        queue = deque([(0, -1)])
        visited.add(0)
        
        # Step 3: Traverse the graph level by level
        while queue:
            node, parent = queue.popleft()
            
            for neighbor in adj[node]:
                # If the neighbor is the node we just came from, ignore it
                if neighbor == parent:
                    continue
                
                # If the neighbor is already visited and it's NOT our parent, 
                # we've found a loop!
                if neighbor in visited:
                    return False
                
                # Otherwise, mark as visited and add to queue with current node as parent
                visited.add(neighbor)
                queue.append((neighbor, node))
                
        # Step 4: Ensure all nodes were reached (fully connected)
        return len(visited) == n

        

        
