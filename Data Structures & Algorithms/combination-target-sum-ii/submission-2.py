class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        current_total = 0
        def backtracker(index,path,current_total):
            if current_total == target:
                results.append(path[:])
                return
            

            if index == len(candidates) or current_total > target:
                return
            
            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i -1]:
                    continue
                
                path.append(candidates[i])
                backtracker(i + 1,path,current_total + candidates[i])
                path.pop()

        candidates.sort()
        backtracker(0,[],0)
        return results
