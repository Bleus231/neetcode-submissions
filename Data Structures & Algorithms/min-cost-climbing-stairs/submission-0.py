class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        results = [cost[0], cost[1]]

        for i in range(2,len(cost)):
            current_cost = cost[i] + min(results[i - 1],results[i - 2])
            results.append(current_cost)

        return min(results[-1], results[-2])
        