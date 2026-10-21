class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #Edge case -> Empty list
        if not nums:
            return 0


        #Array to cache highest subsquence count for every index
        dp = [1] * len(nums)

        #Initialising result variable, can only be a minimum of 1 at this point
        res = 1


        #Creating loop with bottom up approach to go through each index starting from index 1
        for i in range(1,len(nums)):
            
           for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1,dp[i])

            res = max(dp[i],res)
        return res