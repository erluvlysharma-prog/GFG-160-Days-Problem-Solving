class Solution:
    def maxProduct(self, arr):

        current_max = arr[0]
        current_min = arr[0]
        answer = arr[0]

        for i in range(1, len(arr)):

            x = arr[i]

            old_max = current_max
            old_min = current_min

            current_max = max(x,
                               old_max * x,
                               old_min * x)

            current_min = min(x,
                               old_max * x,
                               old_min * x)

            answer = max(answer, current_max)

        return answer