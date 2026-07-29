"""
Approach:
Store Every Consecutive Streak

Problem: 485. Max Consecutive Ones

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
Array Traversal

Approach:
- Traverse the array while counting consecutive 1s.
- Maintain a variable `streak` to count the current run of 1s.
- Whenever a 0 is encountered:
    - Store the completed streak in a list.
    - Reset `streak` to 0.
- After the traversal, append the final streak because the array
  may end with consecutive 1s.
- Return the maximum value from the list of streaks.

Key Insight:
- Every sequence of consecutive 1s is stored.
- After processing the entire array, the largest stored streak
  is the answer.

Example:
nums = [1, 1, 0, 1, 1, 1]

streak = 0
count = []

1 -> streak = 1
1 -> streak = 2
0 -> count = [2], streak = 0
1 -> streak = 1
1 -> streak = 2
1 -> streak = 3

End of array:
count = [2, 3]

Answer = max(count) = 3

Note:
- This solution is simple and easy to understand.
- It stores every streak, which requires O(n) extra space.
- If only the maximum streak is needed, storing all streaks is unnecessary.
"""
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = []
        strek = 0
        for num in nums:
            if num == 0:
                count.append(strek)
                strek = 0
            else:
                strek += 1
        else:
            count.append(strek)
        return max(count)
 
    
"""
Optimal Approach:
Problem: 485. Max Consecutive Ones

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Array Traversal

Approach:
- Traverse the array once.
- Maintain two variables:
    1. count -> length of the current consecutive streak of 1s.
    2. max_count -> longest streak seen so far.
- If the current element is 1:
    - Increase `count`.
- Otherwise:
    - Update `max_count` using the current streak.
    - Reset `count` to 0.
- After the loop, perform one final update because the array may
  end with consecutive 1s.
- Return `max_count`.

Key Insight:
- There is no need to store every streak.
- Only the current streak and the maximum streak found so far
  are required.
- This reduces the extra space from O(n) to O(1).

Why update after the loop?
- If the array ends with 1s, the last streak never encounters a 0,
  so it would never be compared with `max_count` inside the loop.
- The final update ensures the last streak is considered.

Example:
nums = [1, 1, 0, 1, 1, 1]

count = 0
max_count = 0

1 -> count = 1
1 -> count = 2
0 -> max_count = 2, count = 0
1 -> count = 1
1 -> count = 2
1 -> count = 3

End of array:
max_count = max(2, 3) = 3

Answer = 3

Note:
- This is the optimal solution.
- It requires only a single traversal.
- Only two variables are maintained, giving O(1) extra space.
- This is the preferred interview solution.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)    
        return max_count