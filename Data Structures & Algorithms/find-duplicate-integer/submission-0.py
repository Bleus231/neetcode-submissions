class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #Edge case for empty list
        if not nums:
            return 0

        #loop 1 to find collision
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] 

            if slow == fast:
                break

        pointer1 = nums[0]
        pointer2 = slow  # (where they collided in Phase 1)

        # Loop until they meet again at the cycle entrance
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]  # Move 1 step
            pointer2 = nums[pointer2]  # Move 1 step

        # When they meet, pointer1 (or pointer2) holds the      duplicate number!
        return pointer1
        