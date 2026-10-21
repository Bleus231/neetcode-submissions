class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
            
        target = sum(nums) // 2
        memo = {}
        
        def dfs(i, current_sum):
            # Base case: We hit the target exactly!
            if current_sum == target:
                return True
            # Base case: We went over the target or ran out of numbers
            if current_sum > target or i >= len(nums):
                return False
                
            # Check if we've already calculated this state
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            
            # Choice 1: INCLUDE nums[i] in our subset
            # Choice 2: EXCLUDE nums[i] from our subset
            include = dfs(i + 1, current_sum + nums[i])
            exclude = dfs(i + 1, current_sum)
            
            # Save the result in memory so we don't repeat work
            memo[(i, current_sum)] = include or exclude
            return memo[(i, current_sum)]
            
        return dfs(0, 0)