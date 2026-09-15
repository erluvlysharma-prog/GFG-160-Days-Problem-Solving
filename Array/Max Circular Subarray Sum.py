'''You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. 
In a circular array, the subarray can start at the end and wrap around to the beginning. 
Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.'''

class Solution:
    def maxCircularSum(self, arr):
        
        # Find maximum subarray sum
        current_max = arr[0]
        max_sum = arr[0]

        # Find minimum subarray sum
        current_min = arr[0]
        min_sum = arr[0]

        total = arr[0]

        for i in range(1, len(arr)):
            
            # Current maximum subarray
            current_max = max(arr[i], current_max + arr[i])
            max_sum = max(max_sum, current_max)

            # Current minimum subarray
            current_min = min(arr[i], current_min + arr[i])
            min_sum = min(min_sum, current_min)

            # Total array sum
            total += arr[i]

        # If all elements are negative
        if max_sum < 0:
            return max_sum

        # Maximum of normal and circular subarray
        circular_sum = total - min_sum

        return max(max_sum, circular_sum)