"""
Problem: 11. Container With Most Water

Difficulty: Medium

Time Complexity: O(n)

Space Complexity: O(1)

Pattern:
Two Pointers
Greedy

Approach:
- Place one pointer at the beginning (left) and one at the end (right).
- At each step:
    - The width of the container is (right - left).
    - The height of the container is the smaller of the two poles.
    - Compute the current water area:
          curr_water = min(height[left], height[right]) * (right - left)
    - Update the maximum area found so far.
- Move the pointer pointing to the shorter pole:
    - If the left pole is shorter, increment left.
    - Otherwise, decrement right.
- Continue until both pointers meet.
- Return the maximum water area.

Note:
- Starting with the two farthest poles gives the maximum possible width.
- The shorter pole limits the water level, regardless of how tall the other pole is.
- Moving the taller pointer cannot increase the limiting height while the width decreases,
  so it cannot produce a better result.
- Moving the shorter pointer is the only move that may increase the limiting height
  enough to compensate for the reduced width.
- The algorithm examines each pointer at most once, resulting in O(n) time complexity.
- Only a few variables are used, so the extra space complexity is O(1).
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        left = 0
        right = len(height)-1
        while left < right:
            min_height = min(height[left], height[right])
            curr_water = min_height*(right-left)
            max_water = max(curr_water, max_water)
            if height[left] == min_height:
                left += 1
            else:
                right -= 1
        return max_water
            