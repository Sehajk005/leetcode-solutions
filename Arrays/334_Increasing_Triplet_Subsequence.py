"""
Optimal Approach:
Problem: 334. Increasing Triplet Subsequence

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Greedy
Array Traversal

Approach:
- Maintain two variables:
    1. smallest -> the smallest number seen so far.
    2. second_smallest -> the smallest number greater than `smallest`.
- Traverse the array once.
- If the current number is smaller than or equal to `smallest`,
  update `smallest`.
- Otherwise, if it is smaller than or equal to `second_smallest`,
  update `second_smallest`.
- Otherwise, the current number is greater than both `smallest`
  and `second_smallest`, meaning an increasing triplet exists.
  Return True.
- If the traversal finishes without finding such a number,
  return False.

Key Insight:
- We do not need to remember the actual indices or the entire subsequence.
- `smallest` stores the best candidate for the first element.
- `second_smallest` stores the best candidate for the second element.
- Whenever we find a number greater than both, we have:
      smallest < second_smallest < current
  which guarantees an increasing triplet.

Why "<=" instead of "<"?
- Using "<=" allows us to replace duplicate values with the latest occurrence.
- Duplicates cannot contribute to a strictly increasing sequence.
- Updating on equality keeps `smallest` and `second_smallest`
  as small as possible, maximizing the chance of finding a larger
  third element later.

Example:
nums = [2, 1, 5, 0, 4, 6]

smallest = inf
second_smallest = inf

2 -> smallest = 2
1 -> smallest = 1
5 -> second_smallest = 5
0 -> smallest = 0
4 -> second_smallest = 4
6 -> 6 > smallest and second_smallest
     => Increasing triplet found (0 < 4 < 6)

Note:
- This is the optimal solution.
- It requires only a single pass through the array.
- Only two variables are maintained, giving O(1) extra space.
- The algorithm is greedy because it continuously keeps the smallest
  possible first and second elements to maximize the chance of finding
  a valid third element.
"""
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        second_smallest = float('inf')
        for num in nums:
            if num<=smallest:
                smallest = num
            elif num<=second_smallest:
                second_smallest = num
            else:
                return True
        return False