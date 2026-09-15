class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        limit = n // 3
        
        count = {}
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] =1
        result = []
        
        for num in count:
            if count[num] > limit:
                 result.append(num)
                    
        result.sort()
        return result