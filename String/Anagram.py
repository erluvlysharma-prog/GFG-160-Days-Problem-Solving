'''Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

'''

class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        if sorted(s1) == sorted(s2):
           return True
        else:
            False