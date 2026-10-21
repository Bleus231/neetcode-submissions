from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        #list to store edges
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses


        #Loop to add order of unlocks
        for a,b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1
        
        #Load up queue with courses that have no prerequisites
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)

        completed_courses = 0
        # Process the queue (BFS topological sort)
        while queue:
            curr = queue.popleft()
            completed_courses += 1
            # Decrease the in-degree of neighboring courses
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    


        

        return completed_courses == numCourses