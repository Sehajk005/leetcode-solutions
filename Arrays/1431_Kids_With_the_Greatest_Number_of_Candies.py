"""
Problem: 1431. Kids With the Greatest Number of Candies

Difficulty: Easy

Time Complexity: O(n)
- O(n) to find the maximum number of candies.
- O(n) to determine whether each child can have the greatest number of candies.
- Overall: O(n).

Space Complexity:
- Auxiliary Space: O(1)
- Total Space: O(n) (required for the output list)

Pattern:
Array
Simulation
Linear Scan

Approach:
- Find the maximum number of candies among all children.
- Iterate through each child's candies.
- Check whether adding 'extraCandies' makes their total at least equal to the maximum.
- Append True if it does; otherwise, append False.
- Return the resulting boolean list.

Note:
- This is the optimal solution for the problem.
- Every element must be examined at least once to determine the maximum and produce the required output, so O(n) is the best possible time complexity.
- Only constant extra memory is used apart from the required output list.
- The solution avoids creating unnecessary copies of the input array, making it more memory-efficient than approaches that allocate intermediate lists.
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for candie in candies:
            if candie+extraCandies>= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res