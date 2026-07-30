"""
Optimal Approach:
Sliding Window

Problem: 643. Maximum Average Subarray I

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Sliding Window

Approach:
- Compute the sum of the first window of size `k`.
- Initialize `max_sum` with this first window sum.
- Slide the window one element at a time:
    - Add the incoming element to the window sum.
    - Remove the outgoing element from the window sum.
    - Update `max_sum` if the current window sum is larger.
- After processing all windows, divide `max_sum` by `k` to obtain the maximum average.

Key Insight:
- Consecutive windows overlap by `k - 1` elements.
- Instead of recalculating the sum of every window, update the existing window sum by:
    - Subtracting the element leaving the window.
    - Adding the element entering the window.
- This reduces the time complexity from O(n × k) to O(n).

Example:
nums = [1, 12, -5, -6, 50, 3]
k = 4

Initial Window:
[1, 12, -5, -6]
Window Sum = 2
Max Sum = 2

Slide Window:
Remove 1, Add 50
Window Sum = 2 - 1 + 50 = 51
Max Sum = 51

Slide Again:
Remove 12, Add 3
Window Sum = 51 - 12 + 3 = 42
Max Sum = 51

Maximum Average:
51 / 4 = 12.75

Note:
- The window sum is updated in constant time for each slide.
- No extra arrays or slices are created.
- Initializing with the first window sum correctly handles negative numbers.
- This is the optimal solution because it processes each element only once using O(1) extra space.
"""
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        n = len(nums)
        for i in range(k, n):
            window_sum += nums[i]-nums[i-k]
            max_sum = max(max_sum, window_sum)
        return (max_sum)/k
