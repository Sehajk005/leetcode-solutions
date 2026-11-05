"""
Problem: 122. Best Time to Buy and Sell Stock II
Difficulty: Medium

Approach 1: Greedy – Accumulate Profit During Every Increasing Sequence

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Manipulation
* Greedy Algorithm
* Peak and Valley Approach
* Stock Buy and Sell

Approach:

* Initialize `n = len(prices)` to get the number of days.
* Initialize `profit = 0` to maintain the total accumulated profit.
* Initialize `hold = prices[0]` to store the current buying price.
* Start iterating using `i = 0`.
* Use an outer `while` loop to process the array.
* Use an inner `while` loop to identify consecutive increasing prices:
    * Check whether the next day exists (`i + 1 < n`).
    * Check whether the next day's price is greater than the current day's price.
    * If both conditions are satisfied:
        * Add the difference between consecutive prices to `profit`.
        * Increment `i` to move to the next day.
* If `i` reaches the last index, terminate the loop.
* Otherwise:
    * Update `hold = prices[i]` to represent the current buying price.
    * Increment `i` to continue searching for the next increasing sequence.
* Return the accumulated `profit`.

Why it works:

* Whenever the price increases, we accumulate the difference as profit.
* For a continuous increasing sequence, buying at the valley and selling at the peak produces the same profit as adding every consecutive positive difference.
* Decreasing sequences do not contribute to the profit.
* The algorithm captures every profitable upward movement.

Limitation:

* The variable `hold` is unnecessary because it is not used in calculating the profit.
* The nested `while` loops make the implementation slightly more complicated than necessary.
* Requires a non-empty array because `prices[0]` is accessed without checking whether the array is empty.
"""

# Greedy approach: Identify increasing sequences and accumulate consecutive price differences.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        profit = 0
        i = 0
        while True:
            while i+1<n and prices[i]< prices[i+1]:
                profit += prices[i+1] - prices[i]
                i+=1  
            if i == n-1:
                break
            i+=1
        return profit




"""
Problem: 122. Best Time to Buy and Sell Stock II
Difficulty: Medium

Approach 2: Greedy – Add Every Positive Consecutive Difference

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Manipulation
* Greedy Algorithm
* Stock Buy and Sell
* Local Optimal Decisions

Approach:

* Initialize `max_profit = 0` to store the total profit.
* Initialize `buy = prices[0]` to represent the buying price.
* Iterate through the remaining prices using `for sell in prices[1:]`.
* For every price:
    * If `sell > buy`:
        * Calculate the profit by subtracting `buy` from `sell`.
        * Add the profit to `max_profit`.
        * Update `buy = sell` to consider the current price as the next buying price.
    * Otherwise:
        * Update `buy = sell` because the current price is lower than or equal to the previous price.
* Return `max_profit`.

Why it works:

* The algorithm captures every positive difference between consecutive prices.
* If the price increases, the difference is added to the total profit.
* If the price decreases, the previous buying price is replaced with the lower current price.
* This ensures that we always consider the lowest available price before the next increase.
* Multiple transactions are allowed, so accumulating consecutive positive differences gives the maximum possible profit.

Limitation:

* Requires a non-empty array because `prices[0]` is accessed directly.
* The variable `buy` is updated in both branches, so the implementation can be simplified by directly comparing consecutive prices.

Key Observation:

* We do not need to explicitly identify the buying and selling days.
* Every positive consecutive difference contributes to the maximum profit.

"""

# Greedy approach: Add every positive difference between consecutive prices.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell>buy:
                max_profit+=sell-buy
                buy = sell
            else:
                buy = sell
        return max_profit
    
    

"""
Problem: 122. Best Time to Buy and Sell Stock II
Difficulty: Medium

Approach 3: Dynamic Programming – Kadane's Algorithm on Price Differences

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Dynamic Programming
* Kadane's Algorithm
* Array Manipulation
* Maximum Subarray Sum

Approach:

* Initialize `curr = 0` to track the current accumulated profit.
* Initialize `profit = 0` to store the maximum profit encountered.
* Iterate through the array starting from index 1.
* Calculate the difference between consecutive prices:
    * `diff = prices[i] - prices[i-1]`
* Update the current accumulated profit:
    * `curr = max(curr, curr + diff)`
* Update the maximum profit:
    * `profit = max(profit, curr)`
* Return `profit`.

Why it works:

* The difference array represents the daily price changes.
* Positive differences represent potential profits, while negative differences represent losses.
* Kadane's algorithm identifies the maximum sum of a contiguous subarray of differences.
* However, for this problem, we can perform multiple transactions.
* Every positive difference can be collected independently, meaning the maximum profit is actually the sum of all positive differences.
* The implementation of Kadane's algorithm also produces this result because `curr` never becomes negative.

Limitation:

* Kadane's algorithm is designed to find the maximum sum of a contiguous subarray.
* This problem allows multiple independent transactions, so finding a maximum subarray is unnecessary.
* The algorithm works, but it solves a more restrictive problem than required.
* It also requires an empty-array-safe implementation, although this particular loop handles an empty array correctly.

Key Observation:

* Unlike LeetCode 121 (Best Time to Buy and Sell Stock), where only one transaction is allowed, LeetCode 122 allows unlimited transactions.
* Therefore, we can accumulate all positive consecutive differences instead of finding one maximum subarray.

"""

# Dynamic Programming approach: Apply Kadane's algorithm to consecutive price differences.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curr = 0
        profit = 0
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            curr = max(curr, curr+diff)
            profit = max(profit, curr)
        return profit
    
    
"""
Problem: 122. Best Time to Buy and Sell Stock II
Difficulty: Medium

Approach 4: Greedy – Sum of All Positive Consecutive Differences

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Manipulation
* Greedy Algorithm
* Stock Buy and Sell
* Mathematical Optimization

Approach:

* Initialize `max_profit = 0` to maintain the total accumulated profit.
* Iterate through the array starting from index 1.
* For every element:
    * Calculate the difference between the current day's price and the previous day's price:
        * `prices[i] - prices[i-1]`
    * Use `max(0, difference)` to ensure that only positive differences contribute to the profit.
    * Add the result to `max_profit`.
* Return `max_profit`.

Why it works:

* If the current day's price is greater than the previous day's price, the difference represents a profitable opportunity.
* If the current day's price is lower than or equal to the previous day's price, the difference contributes 0 profit.
* Since multiple transactions are allowed, we can accumulate every positive consecutive difference.
* Using `max(0, difference)` automatically ignores decreasing or unchanged prices.
* This guarantees that we capture every possible profitable upward movement.

Advantages:

* No need to explicitly maintain buying and selling prices.
* No need for nested loops or additional variables.
* Handles empty and single-element arrays without additional conditions.
* Provides a concise implementation of the greedy strategy.

Key Observation:

* Instead of writing an explicit `if-else` condition to check whether the price increased, `max(0, difference)` handles both cases.
* This is mathematically equivalent to adding only positive consecutive price differences.

"""

# Greedy approach: Sum all positive consecutive price differences using max(0, difference).   
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i]-prices[i-1])
        return max_profit