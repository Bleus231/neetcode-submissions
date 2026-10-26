class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0
        count = 0
        sorted_list = sorted(nums)
        print(sorted_list)
        for i in range(len(nums)):
            res = i ^ sorted_list[i]
            print(res)
            if res != 0:
                return i
            count += 1
        

        return count