class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]

        if n == 1:
            return [0,1]
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        
        

        for i in range(2,n + 1):
            one = i
            count = 0
            while one > 0:
                one = one & (one - 1)
                count += 1
            dp[i] = count

        return dp