class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_money = [nums[0],max(nums[0], nums[1])]

        for i in range(2,len(nums)):
            current_max_money =max(nums[i] + max_money[i - 2],max_money[i-1])
            max_money.append(current_max_money)

        return max(max_money[-1],max_money[-2])
            
        