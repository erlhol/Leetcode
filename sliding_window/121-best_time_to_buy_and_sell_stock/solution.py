class Solution:
    # Solution explaination:
    # Iterate through all of the prices, always finding the minimum price.
    # If the current price is cheaper than the cheapest price found so far,
    # update the cheapest price
    # If the profit is higher than what we have found earlier, then
    # update the max_profit.

    # Runtime is then only O(n), since we always compare with the cheapest price only

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheapest = prices[0]
        for price in prices[1:]:
            if price < cheapest:
                cheapest = price
            
            profit = price - cheapest
            if profit > max_profit:
                max_profit = profit
        return max_profit
        