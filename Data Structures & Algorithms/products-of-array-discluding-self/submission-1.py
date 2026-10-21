class Solution:
    def productLeft(self,nums: List[int], position: int) -> int:
        res = 1
        for i in range(position):
            res = res * nums[i]

        return res


    def productRight(self,nums: List[int], postion: int) -> int:
        res = 1
        right = postion + 1
        for right in range(right,len(nums)):
            res = res * nums[right]

        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            res.append(self.productLeft(nums,i) * self.productRight(nums,i))


        return res


