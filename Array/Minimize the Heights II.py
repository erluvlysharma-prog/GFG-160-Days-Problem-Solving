'''Given an array arr[] representing the heights of n towers and a positive integer k. 
For each tower, perform exactly one of the following operations exactly once:

Increase its height by k, or
Decrease its height by k.
After performing the operation on every tower, the height of any tower must not become negative.

Return the minimum possible difference between the heights of the tallest and the shortest towers after modifying all the towers.'''

class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()

        n = len(arr)

        answer = arr[n - 1] - arr[0]

        for i in range(n - 1):

            if arr[i + 1] - k < 0:
                continue

            maximum = max(arr[i] + k, arr[n - 1] - k)

            minimum = min(arr[0] + k, arr[i + 1] - k)

            difference = maximum - minimum

            answer = min(answer, difference)

        return answer