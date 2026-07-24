"""
Problem: 283. Move Zeroes

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(n)

Pattern:
Array
Simulation
Extra Arrays

Approach:
- Traverse the array once.
- Store all non-zero elements in one list.
- Store all zero elements in another list.
- Concatenate the non-zero list followed by the zero list.
- Return the combined list.

Note:
- The array is traversed only once, resulting in O(n) time complexity.
- Two additional lists are used to store all elements, requiring O(n) extra space.
- This solution does NOT satisfy the in-place requirement of the original LeetCode problem because:
    - nums = non_zeroes + zeroes only reassigns the local variable.
    - The original input list remains unchanged.
- To modify the original list using this approach, use:
      nums[:] = non_zeroes + zeroes
- The optimal solution uses the Two Pointers pattern:
    - Move all non-zero elements forward while maintaining their order.
    - Fill the remaining positions with zeros.
    - Achieves O(n) time complexity and O(1) extra space.
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        non_zeroes = []
        for num in nums:
            if num==0:
                zeroes.append(num)
            else:
                non_zeroes.append(num)
        nums[:] = non_zeroes+zeroes
        

"""
Problem: 283. Move Zeroes

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(1)

Pattern:
Array
Two Pointers
In-place Modification

Approach:
- Use two pointers:
    - i scans every element in the array.
    - j tracks the position where the next non-zero element should be placed.
- Traverse the array once:
    - If nums[i] is non-zero, copy it to nums[j] and increment j.
- After all non-zero elements have been moved to the front,
  fill the remaining positions from j to the end with zeros.

Note:
- Each element is visited exactly once, giving O(n) time complexity.
- The array is modified in-place, requiring O(1) extra space.
- This approach preserves the relative order of all non-zero elements.
- Writing nums[j] = nums[i] even when i == j is harmless and keeps the implementation simple.
- The statement:
      nums[j:] = [0] * len(nums[j:])
  replaces all remaining positions with zeros in a single operation.
- This is one of the standard optimal solutions for the Move Zeroes problem.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j] = nums[i]
                j+=1
        nums[j:] = [0]*len(nums[j:])