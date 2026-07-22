"""
Problem: 605. Can Place Flowers

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(1)

Pattern:
Greedy
Array Traversal
Simulation

Approach:
- Handle the single-element flowerbed separately.
- Check if a flower can be planted at the first position.
- Check each middle position:
    - Plant only if the current plot and both neighbors are empty.
- Check if a flower can be planted at the last position.
- Decrease n whenever a flower is planted.
- Return True if all required flowers have been planted; otherwise return False.

Note:
- This is a greedy approach because it plants a flower as soon as a valid position is found.
- The solution divides the flowerbed into three cases:
    1. First position
    2. Middle positions
    3. Last position
- Although efficient (O(n)), it relies on multiple boundary checks and special cases, making the implementation longer and more prone to edge-case mistakes.
"""
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n -= 1
            return True if n <= 0 else False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
        return True if n <= 0 else False
    
    
"""
Problem: 605. Can Place Flowers

Difficulty: Easy

Time Complexity: O(n)

Space Complexity: O(1)

Pattern:
Greedy
Array Traversal
Simulation

Approach:
- Traverse the flowerbed from left to right exactly once.
- For every position:
    - Consider the left neighbor (prev), current plot (curr), and right neighbor (next).
    - Treat missing neighbors at the boundaries as empty plots.
    - If all three are empty, plant a flower and decrement n.
- Return True immediately once n <= 0.
- If the traversal ends before planting all flowers, return False.

Note:
- This is the standard greedy solution.
- It handles every position using the same logic, eliminating separate cases for the first and last plots.
- Treating the boundaries as virtual empty plots simplifies the implementation and reduces edge-case handling.
- The algorithm is both optimal and easy to reason about, requiring only a single pass through the flowerbed.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        curr = flowerbed[0]
        prev = 0
        next = 0
        length = len(flowerbed)
        for i in range(length):
            if i<length-1:
                next = flowerbed[i+1]
            else:
                next = 0
            if prev == 0 and curr == 0 and next == 0:
                n-=1
                flowerbed[i] = 1
            if n<=0:
                return True
            prev = flowerbed[i]
            curr = next
        return False