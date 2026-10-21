class Solution:
   def permute(self, nums: List[int]) -> List[List[int]]: 
    results = [] 
    
    
    
    def backtrack(index,path): 

        #Condition for when backtrack is at final step 
        
        if len(path) == len(nums): 
            if path[:] not in results:

                results.append(path[:]) 
            return

        for i in range(len(nums)):  
        #Decision 1 -> take current number 

            if nums[i] not in path:
                path.append(nums[i])

                backtrack(index + 1,path) 
                path.pop() 

    backtrack(0,[]) 
    
    return results
        