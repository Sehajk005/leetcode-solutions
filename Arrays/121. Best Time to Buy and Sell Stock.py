"""
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Approach 1: Brute Force (Checking Every Buy and Sell Pair)

Time Complexity: O(n²)
Space Complexity: O(1)

Pattern:

* Array Traversal
* Brute Force
* Pairwise Comparison
* Optimization

Approach:

* Initialize `max = 0` to store the maximum profit.
* Use the outer loop to select each day `i` as the buying day.
* Use the inner loop to select every day `j` after day `i` as the selling day.
* Calculate the profit using `prices[j] - prices[i]`.
* If the calculated profit exceeds `max`, update `max`.
* Return `max` after checking every valid pair.

Why it works:

* Every possible buying and selling pair is checked.
* The inner loop starts at `i + 1`, ensuring that selling happens after buying.
* The maximum profit among all valid pairs is returned.
* If no profitable transaction exists, the answer remains 0.

Limitation:

* The nested loops result in O(n²) time complexity.
* Repeatedly checking all possible pairs is inefficient for large arrays.
* The variable name `max` shadows Python's built-in `max()` function. Prefer `max_profit`.

"""

# Brute force: Check every possible buy-sell pair.
class Solution(object):
    def maxProfit(self, prices):
        max = 0 
        for i in range(len(prices)):
            for j in range (i + 1, len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max
        

"""
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Approach 2: Greedy (Track the Minimum Buying Price)

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Traversal
* Greedy Algorithm
* Running Minimum
* Single-Pass Optimization

Approach:

* Initialize `buy = prices[0]` to store the minimum price encountered so far.
* Initialize `profit = 0` to store the maximum profit.
* Iterate through each price in `prices[1:]`, treating it as a potential selling price.
* If `sell < buy`, update `buy = sell` because a lower buying price has been found.
* Calculate the potential profit using `sell - buy`.
* If the potential profit exceeds `profit`, update `profit`.
* Return `profit` after completing the traversal.

Why it works:

* Buying at the lowest price encountered so far maximizes the profit for a given selling price.
* Every price is considered as a potential selling price.
* The algorithm updates the minimum buying price and maximum profit in a single pass.
* Initializing `profit = 0` ensures that no transaction is made when all prices decrease.

Limitation:

* `prices[0]` assumes that the input array is non-empty.
* For an empty array, an additional check is required before accessing the first element.

"""

# Greedy: Maintain the lowest buying price and the maximum profit. 
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        for sell in prices[1:]:
            if sell<buy:
                buy = sell
            if sell-buy>profit:
                profit = sell-buy
        return profit
    

"""
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Approach 3: Kadane's Algorithm on Price Differences

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Traversal
* Kadane's Algorithm
* Maximum Subarray Sum
* Difference Array
* Dynamic Programming

Approach:

* Initialize `curr = 0` to store the maximum profit of the current contiguous section of price differences.
* Initialize `profit = 0` to store the overall maximum profit.
* Iterate from index `1` to the end of `prices`.
* Calculate the difference between consecutive prices using `diff = prices[i] - prices[i-1]`.
* Update `curr = max(0, curr + diff)`:
    * Extend the current section if doing so produces a positive profit.
    * Reset `curr` to 0 if the accumulated profit becomes negative.
* Update `profit = max(profit, curr)` to maintain the best profit found.
* Return `profit`.

Why it works:

* Each difference represents the daily gain or loss.
* The sum of consecutive differences equals the selling price minus the buying price over that period.
* Finding the maximum-sum contiguous subarray therefore finds the maximum possible stock profit.
* Resetting `curr` to 0 discards an unprofitable section and allows a new transaction to begin.

Limitation:

* The approach transforms the problem into a maximum-subarray problem, making it less intuitive than directly tracking the minimum buying price.
* It requires understanding the relationship between consecutive price differences and total profit.

"""

# Kadane's algorithm: Find the maximum subarray sum of consecutive price differences.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curr = 0
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            curr = max(0, curr+diff)
            profit = max(profit, curr)
        return profit
    

"""
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Approach 4: Greedy (Using min() and max())

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Traversal
* Greedy Algorithm
* Running Minimum
* Running Maximum
* Single-Pass Optimization

Approach:

* Initialize `min_price = prices[0]` to store the minimum price encountered so far.
* Initialize `max_profit = 0` to store the maximum profit.
* Iterate through every price in `prices[1:]`.
* Update `min_price = min(min_price, price)` to maintain the lowest price seen so far.
* Calculate the potential profit using `price - min_price`.
* Update `max_profit = max(max_profit, price - min_price)` to retain the highest profit.
* Return `max_profit`.

Why it works:

* The minimum price encountered so far represents the best buying price available before or on the current day.
* Each current price is evaluated as a potential selling price.
* The `min()` and `max()` functions simplify the comparisons used in the greedy approach.
* The algorithm processes the array once while maintaining only two variables.

Limitation:

* `prices[0]` assumes that the array is non-empty.
* This approach uses the same greedy principle as Approach 2; the main difference is that it expresses the updates more concisely using built-in functions.

"""

# Optimized greedy: Use min() and max() to update the buying price and profit.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit