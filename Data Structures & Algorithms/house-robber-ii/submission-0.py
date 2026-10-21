class Solution:
    def rob(self, nums: List[int]) -> int:

        # If only 1 element then return it
        if (len(nums) < 2):
            return nums[0]
        
        # Create 2 arrays
        # 1) Including first index and not last
        include_first = []
        # 2) Not including first index
        include_last = []

        # Populate both arrays
        for i in range(0,len(nums) - 1):
            include_first.append(nums[i])
            include_last.append(nums[i + 1])

        def rob_helper(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]

            max_money = [nums[0],max(nums[0], nums[1])]

            for i in range(2,len(nums)):
                current_max_money = max(nums[i] + max_money[i - 2],max_money[i-1])
                max_money.append(current_max_money)

            return max(max_money[-1],max_money[-2])

        include_first_max = rob_helper(include_first)
        include_last_max = rob_helper(include_last)

        return max(include_first_max,include_last_max) 


