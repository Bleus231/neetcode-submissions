class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
             return 1
        if n == 2:
             return 2


        
        step_results = [0,1,2]

        for i in range(len(step_results),n+1):
    
            current_step = step_results[i-1] +  step_results[i-2]
            step_results.append(current_step)

        return step_results[n]           