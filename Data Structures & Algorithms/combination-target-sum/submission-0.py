class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current_set = []
        current_total = 0       

        def backtracking(index,path,current_total):
            
            #Out of bounds edge case
            if index == len(nums):
                return

               

            #If current set equals target num then add a copy of the set to results
            if current_total == target:
                results.append(path[:])
                return


            
            #If current total is greater than target, no point carrying on
            if current_total > target:
                return
                
                
            #Decision 1
            path.append(nums[index])
            current_total += nums[index]
            backtracking(index,path,current_total)  

            #Decision 2
            path.pop()
            current_total -=nums[index]
            backtracking(index + 1,path,current_total)

            

        backtracking(0,current_set,current_total)
        return results

            



        