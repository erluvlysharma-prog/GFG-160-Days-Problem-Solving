'''Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.'''

class Solution:
    def minChar(self, s):
        # code here
        rev = s[::-1]
        combined = s + '$' + rev
        
        lps = [0] * len(combined)
        
        j= 0
        
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j -1]
                
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j
        return len(s) - lps[-1]
   