class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Edge cases
        #1) empty array return 0
        if not nums:
            return 0
        
        #Safer to initialize to first element than 0
        res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        #if only one element
        if len(nums) == 1:
            return res
        
              
        for i in range(1,len(nums)):

            num = nums[i]
                
                # Because a negative number flips min/max, temporarily store curr_max
            temp_max = curr_max
            
            curr_max = max(num, num * curr_max, num *   curr_min)
            curr_min = min(num, num * temp_max, num * curr_min)
                
            res = max(res, curr_max)
            
        return res


            
