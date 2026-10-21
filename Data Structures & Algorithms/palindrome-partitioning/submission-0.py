class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        def backtrack(string,index,path):
            


            #Dealing with edge cases
            if index >= len(s):
                results.append(path[:])
                return
            
            for i in range(index,len(s)):
                substring = s[index:i + 1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(substring,i + 1,path)
                    path.pop()
            
            
            

        backtrack("",0,[])
        return results 