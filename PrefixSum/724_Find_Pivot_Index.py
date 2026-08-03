"""
Optimal Approach:
Prefix Sum

Problem: 724. Find Pivot Index

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Prefix Sum

Approach:
- Compute the total sum of the array.
- Maintain a running prefix sum (left sum).
- For each index:
    right sum = total sum - left sum - current element.
- If left sum equals right sum, that index is the pivot.
- Otherwise, update the prefix sum and continue.

Key Formula:
leftSum = prefixSum
rightSum = totalSum - prefixSum - nums[i]

Why it works:
- The prefix sum stores the sum of elements to the left.
- Subtracting the prefix sum and current element from the total gives the sum of elements to the right.
- Each index is checked exactly once.

Common Mistakes:
- Iterating only until n-2 and missing the last index.
- Incorrectly returning the loop variable after the loop.
- Recomputing suffix sums repeatedly, leading to O(n²) solutions.
"""
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        prefixSum = 0
        for i in range(len(nums)):
            suffixSum = totalSum - prefixSum - nums[i]
            
            if prefixSum ==suffixSum:
                return i

            prefixSum += nums[i]
        return -1