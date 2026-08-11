"""
Approach 1:
Brute Force

Problem: 735. Asteroid Collision

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Pattern:
Simulation

Approach:

* Make a copy of the asteroids list.
* Repeatedly scan the list looking for a collision.
* A collision occurs only when:

  * The left asteroid is moving right (`> 0`).
  * The right asteroid is moving left (`< 0`).
* When a collision is found:

  * If the left asteroid is larger, remove the right asteroid.
  * If the right asteroid is larger, remove the left asteroid.
  * If both are equal, remove both asteroids.
* After resolving one collision, start scanning again.
* Stop when a complete pass produces no collision.

Key Insight:

* Only adjacent asteroids moving toward each other can collide.
* After removing an asteroid, new neighboring asteroids may become
  adjacent and collide.
* Therefore, the list must be scanned repeatedly until no collisions
  remain.

Example:
asteroids = [5, 10, -5]

Process:

[5, 10, -5]

10 and -5 collide.
10 is larger → remove -5.

[5, 10]

No more collisions.

Final Result:
[5, 10]

Why O(n²)?

* In the worst case, many collisions may occur.
* After each collision, the list is modified and scanned again.
* A scan can take O(n).
* Up to O(n) collisions/scans can occur.
* Therefore, worst-case time complexity is O(n²).

Note:

* pop(i) is also O(n) because elements after index i
  must be shifted.
* This makes the brute-force approach inefficient for large inputs.
* This approach is useful for understanding the collision process,
  but it is not the optimal solution.

Important Pattern:

"Repeatedly find and resolve conflicts"
↓
SIMULATION
↓
Repeated scanning
↓
O(n²)
---

Comparison:

Brute Force:

* Repeatedly scans the entire list.
* Direct simulation.
* Easier to understand initially.
* Time: O(n²)
* Space: O(n)

Stack:

* Maintains only surviving asteroids.
* Resolves collisions immediately.
* Handles multiple collisions using `while`.
* Time: O(n)
* Space: O(n)

Final Takeaway:

If a problem involves elements moving toward each other and
previous elements can be removed by a newly processed element,
think:

"Can I maintain the surviving elements in a STACK?"

For Asteroid Collision:

Current asteroid
↓
Possible collision
↓
Compare with stack top
↓
Destroy smaller
↓
Continue if current survives
↓
Push if no collision
"""
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroids = asteroids[:]
        while True:
            collision = False
            for i in range(len(asteroids) - 1):
                if asteroids[i] > 0 and asteroids[i + 1] < 0:
                    collision = True
                    if abs(asteroids[i]) > abs(asteroids[i + 1]):
                        asteroids.pop(i + 1)
                    elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                        asteroids.pop(i)
                    else:
                        asteroids.pop(i)
                        asteroids.pop(i)
                    break
            if not collision:
                break
        return asteroids
    
"""
Approach 2:
Stack

Problem: 735. Asteroid Collision

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:
Stack

Approach:

* Maintain a stack using a list called output.
* Traverse the asteroids from left to right.
* Add asteroids to the stack when there is no collision.
* A collision can only occur when:

  * The current asteroid is moving left (`num < 0`).
  * The top asteroid in the stack is moving right (`output[-1] > 0`).
* Compare the sizes of the two colliding asteroids.

Collision Cases:

1. Current asteroid is larger:

   output[-1] < -num

   * Pop the top asteroid.
   * Continue checking because the current asteroid may
     collide with another asteroid behind it.

2. Both asteroids are equal:

   output[-1] == -num

   * Pop the top asteroid.
   * The current asteroid is also destroyed.
   * Break out of the collision loop.

3. Stack asteroid is larger:

   output[-1] > -num

   * The current asteroid is destroyed.
   * Do not add it to the stack.

4. No collision:

   * Add the current asteroid to the stack.

Key Insight:

* The stack contains the surviving asteroids from left to right.
* The top of the stack represents the closest surviving asteroid
  that could collide with the current asteroid.
* A left-moving asteroid can only collide with a right-moving asteroid
  immediately before it.
* If the current asteroid destroys the top asteroid, it may continue
  moving left and collide with the next asteroid.
* Therefore, a `while` loop is required.

Example:
asteroids = [10, 2, -5]

Process:

10 → [10]

2 → [10, 2]

-5 arrives.

2 and -5 collide.
5 > 2 → remove 2.

[10]

Now -5 can collide with 10.

10 > 5 → -5 is destroyed.

Final Result:
[10]

Why O(n)?

* Every asteroid is added to the stack at most once.
* Every asteroid can be removed from the stack at most once.
* Although a `while` loop is used, an asteroid that is popped
  never comes back.
* Therefore, the total number of stack operations is O(n).

Note:

* `output` acts as a stack.
* `append()` → push asteroid onto the stack.
* `pop()` → remove the top asteroid.
* `num < 0 < output[-1]` identifies a possible collision.
* The `while` loop handles multiple consecutive collisions.
* The cleaner version avoids repeatedly checking the same
  direction conditions.

Important Pattern:

"Process elements while previous elements may be destroyed"
↓
STACK
↓
LIFO (Last In, First Out)
↓
O(n)
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        for num in asteroids:
            while output and abs(num) > abs(output[-1]) and num<0 and output[-1]>0:
                output.pop()
            if output and abs(num) == abs(output[-1]) and num<0 and output[-1]>0:
                output.pop()
            elif output and abs(num) < abs(output[-1]) and num<0 and output[-1]>0:
                continue
            else:
                output.append(num)
        return output

"""Cleaner Version"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        for num in asteroids:
            while output and num < 0 < output[-1]:
                if output[-1] < -num:
                    output.pop()
                    continue
                elif output[-1] == -num:
                    output.pop()
                break
            else:
                output.append(num)
        return output