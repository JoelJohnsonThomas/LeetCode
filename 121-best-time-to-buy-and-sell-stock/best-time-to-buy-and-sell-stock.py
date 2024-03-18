class Solution(object):
    def maxProfit(self, prices):
      left = 0
      right =1
      max_price =0
      while right<len(prices):
        currentmax_price = prices[right] - prices[left]
        if prices[left]<prices[right]:
          max_price = max(currentmax_price,max_price)
        else:
          left = right
        right+=1
      return max_price