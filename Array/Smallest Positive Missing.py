'''You are given an integer array arr[]. 
Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.'''

class Solution:
    def missingNumber(self, arr):
        # code here
        n =  len(arr)
        
        i = 0
        while i < n:
            if 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                i += 1
        
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
                
        return n + 1