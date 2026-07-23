"""
Problem: 1929. Concatenation of Array

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(n)

Pattern:
Array
Simulation

Approach:
- Create a new array by concatenating the original array with itself.
- The first n elements are copied from nums.
- The next n elements are another copy of nums.
- Return the resulting array.

Note:
- In Python, `nums + nums` creates a new list containing two consecutive
  copies of the original list.
- Since a new array of size 2n is required, O(n) extra space is unavoidable.
- This is the most concise and optimal Python solution.
"""
from git import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums