class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #If list is empty return -1
        if not coins:
            return -1


        #Create pre populated array , Create infinity baseline value placeholders
        min_amount = [amount + 1] * (amount + 1)

        #Base case for first element
        min_amount[0] = 0
        for i in range(1,len(min_amount)):

            for coin in coins:

                #check if current value is bigger than amount 
                if i < coin:
                    continue

                min_amount[i] = min(min_amount[i], min_amount[i - coin] + 1)

        if min_amount[-1] > amount:
            min_amount[-1] = -1
            
                
            
        return min_amount[-1]
        