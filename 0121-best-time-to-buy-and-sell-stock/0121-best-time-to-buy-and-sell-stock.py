class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the variable to track the minimum price encountered so far.
        # Start with infinity to ensure that any price will be less than this
        # initial value.
        min_price = float("inf")

        # Initialize max_profit to 0. This will hold the highest profit that can
        # be made.
        max_profit = 0

        # Iterate through the list of prices to find the maximum profit.
        for price in prices:

            # If the current price is less than the minimum price seen so far,
            # update the minimum price.
            if price < min_price:
                min_price = price

            # Calculate the profit if we were to sell at the current price.
            profit = price - min_price

            # If the profit is greater than the current max_profit, update
            # max_profit.
            if profit > max_profit:
                max_profit = profit

        # After iterating through the list, return the maximum profit found.
        return max_profit
