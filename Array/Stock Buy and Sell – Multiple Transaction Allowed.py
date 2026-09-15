'''Given an integer array prices[], where prices[i] is the price of a given stock on the ith day. 
Each day you may decide to either buy or sell the stock at price[i], 
you can even buy and sell the stock on the same day, return the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.'''

class Solution:
    def maxProfit(self, prices):
        # code here
        profit = 0
        
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i - 1]
        return profit