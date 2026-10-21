class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert list to a set for O(1) lookups
        word_set = set(wordDict)
        
        # dp[i] represents whether the substring s[:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string is valid
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If prefix up to j is valid and s[j:i] is a dictionary word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[len(s)]