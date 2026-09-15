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