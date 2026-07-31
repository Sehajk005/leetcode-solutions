"""
Approach:
Prefix Sum (Store All Altitudes)

Problem: 1732. Find the Highest Altitude

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
Prefix Sum

Approach:
- Start at altitude 0.
- Create a list `altitudes` initialized with `[0]`.
- Traverse the `gain` array:
    - Add the current gain to the running altitude.
    - Append the new altitude to the `altitudes` list.
- After processing all gains, return the maximum value in `altitudes`.

Key Insight:
- Each altitude is the cumulative sum (prefix sum) of all previous gains.
- By storing every altitude, the highest altitude can be found by taking the maximum of the list.
- This approach is straightforward and useful when all intermediate altitudes are needed.

Example:
gain = [-5, 1, 5, 0, -7]

Start:
Altitude = 0
altitudes = [0]

After -5:
Altitude = -5
altitudes = [0, -5]

After +1:
Altitude = -4
altitudes = [0, -5, -4]

After +5:
Altitude = 1
altitudes = [0, -5, -4, 1]

After +0:
Altitude = 1
altitudes = [0, -5, -4, 1, 1]

After -7:
Altitude = -6
altitudes = [0, -5, -4, 1, 1, -6]

Highest Altitude:
max(altitudes) = 1

Note:
- Every altitude is stored in a separate list.
- Finding the maximum requires another traversal of the list.
- This solution is easy to understand but uses O(n) extra space.
"""
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        alt = 0
        for g in gain:
            alt += g
            altitudes.append(alt)
        return max(altitudes)
    
"""
Optimal Approach:
Running Prefix Sum

Problem: 1732. Find the Highest Altitude

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Prefix Sum

Approach:
- Initialize:
    - `curr_alt = 0` (current altitude)
    - `max_alt = 0` (highest altitude seen so far)
- Traverse the `gain` array:
    - Update the current altitude by adding the current gain.
    - Update `max_alt` if the current altitude is higher.
- Return `max_alt`.

Key Insight:
- The problem only asks for the highest altitude, not every altitude.
- Instead of storing all prefix sums, keep only:
    - The current altitude.
    - The maximum altitude encountered so far.
- This eliminates the need for an extra array and reduces space complexity to O(1).

Example:
gain = [-5, 1, 5, 0, -7]

Start:
curr_alt = 0
max_alt = 0

After -5:
curr_alt = -5
max_alt = 0

After +1:
curr_alt = -4
max_alt = 0

After +5:
curr_alt = 1
max_alt = 1

After +0:
curr_alt = 1
max_alt = 1

After -7:
curr_alt = -6
max_alt = 1

Answer:
1

Note:
- Each gain is processed exactly once.
- No additional list is created.
- The running altitude and maximum altitude are updated in constant time.
- This is the optimal solution because it achieves O(n) time using only O(1) extra space.
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = 0
        for g in gain:
            curr_alt += g
            max_alt = max(curr_alt, max_alt)
        return max_alt