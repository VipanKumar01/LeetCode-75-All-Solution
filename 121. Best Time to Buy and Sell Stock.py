class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
#         This is My Solution Only One Test Case is not Pass out
#############################################################
        """
        minimum = min(i for i in prices)
        # maximum = max(i for i in prices)
        
        min_index = prices.index(minimum)
        maximum = max(prices[i] for i in range(min_index,len(prices)))
        max_index = prices.index(maximum)
        
        
        if min_index < max_index:
            profit = maximum-minimum
            return profit
        else:
            return 0
        """
  ##########################################################
  
  
        min_ = 2**31
        max_ = 0
        for i in prices:
            if i < min_:
                min_ = i
            if i-min_ > max_:
                max_ = i - min_
        return max_
