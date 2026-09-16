'''Given a string s consisting of lowercase English Letters. 
return the first non-repeating character in s. 
If there is no non-repeating character, return '$'.'''

def nonRepeatingChar(self, s):

        # Dictionary to store character counts
        freq = {}

        # STEP 1: Count each character
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # STEP 2: Find the first character whose count is 1
        for ch in s:
            if freq[ch] == 1:
                return ch

        # STEP 3: No non-repeating character
        return '$'