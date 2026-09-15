class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        
        
        # Step 1: Find the smaller element from the right
        i = n - 2
        
        
        while i >= 0 and arr [i] >= arr[i+1]:
            i -= 1
            
            
        # Step 2: Find a number greater than arr[i]
        if i >= 0:
            j = n - 1
            
            while arr[j] <= arr[i]:
                j -= 1
        
            
            #Swap
            arr[i], arr[j] = arr[j], arr[i]
            
            
        # Step 3: Reverse the part after i
        arr[i+1:] = reversed(arr[i+1:])
        