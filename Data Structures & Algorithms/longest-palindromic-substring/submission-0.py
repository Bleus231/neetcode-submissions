class Solution:
        def longestPalindrome(self, s: str) -> str:
                
                #variable to store len of list to avoid repeated typing
                n = len(s)
                #Edge case where length of n is less than or equal to 1
        
                if n <= 1:
                        return s
                
                l = 0
                r = 0
                result = 0
                longest_palindrome = ""
                def expand(left,right):
                        while left >= 0 and right < n and s[left] == s[right]:
                                left -= 1
                                right +=1
                        return s[left + 1:right]
                


                for i in range(len(s)):
                        # Case 1: Odd length palindromes (e.g., "aba" centered at 'b')
                        p1 = expand(i, i)
                        if len(p1) > len(longest_palindrome):
                                longest_palindrome = p1

                        # Case 2: Even length palindromes (e.g., "abba" centered between 'b' and 'b')
                        p2 = expand(i, i + 1)
                        if len(p2) > len(longest_palindrome):
                                longest_palindrome = p2

                        
                return longest_palindrome


