'''Given two strings, a text string txt and a pattern string pat, both consisting of lowercase English alphabets. 
Return the starting indices (0-based) of all the occurrences of the pattern string pat in the text string txt.

Note: Return an empty list in case of no occurrences of pattern.'''

class Solution:
    def search(self, pat, txt):
        # code here
        ans = []
        
        for i in range(len(txt) - len(pat) + 1):
            if txt[i:i +len(pat)] == pat:
                ans.append(i)
                
        return ans