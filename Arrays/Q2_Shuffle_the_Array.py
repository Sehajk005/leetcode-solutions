"""
Problem: 1470. Shuffle the Array

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(n)

Pattern:
Array Traversal
Simulation

Approach:
- Initialize an empty answer array.
- Traverse the first half of the array (x1 to xn).
- For each index i:
    - Append nums[i] (the current x element).
    - Append nums[i + n] (the corresponding y element).
- Continue until all pairs have been processed.
- Return the shuffled array.

Note:
- The input array is divided into two equal halves:
    - First half:  [x1, x2, ..., xn]
    - Second half: [y1, y2, ..., yn]
- Each iteration appends one element from each half, preserving
  the required alternating order.
- Every element is visited exactly once, resulting in O(n) time.
- Since a new array of size 2n is created, O(n) extra space is required.
"""
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr