from typing import List

# O(n)
def maxProfit(prices: List[int]) -> int:
    minimum, maximum = prices[0], prices[0]
    prev_profit = 0
    
    for price in prices:
      if price > maximum:
        maximum = price
      elif price < minimum:
        prev_profit = max(prev_profit, maximum -  minimum)
        minimum, maximum = price, price
      

    return max(prev_profit, maximum - minimum)


print(maxProfit([1,2]))