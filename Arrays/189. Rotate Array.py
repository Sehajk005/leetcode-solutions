"""
Problem: 189. Rotate Array
Difficulty: Medium
Approach 1: Using pop() and a Temporary List

Time Complexity: O(n) in the worst case
Space Complexity: O(n)

Pattern:

* Array Manipulation
* Stack-Like Operations
* Temporary Storage

Approach:

* Return immediately if `nums` is empty.
* Calculate `k = k % len(nums)` to handle rotations greater than the array length.
* Create an empty list `arr` to store the last `k` elements.
* Use `nums.pop()` to remove the last element and append it to `arr`, repeating `k` times.
* Reverse `arr` using `arr[::-1]` to restore the original relative order of the removed elements.
* Insert the reversed elements at the beginning of `nums` using `nums[0:0] = arr[::-1]`.

Why it works:

* Each `pop()` extracts the last element, which belongs at the beginning after a right rotation.
* Popping elements reverses their order, so `arr[::-1]` restores their original relative order.
* Inserting these elements at index 0 shifts the remaining elements to the right.

Limitation:

* Removing elements from the end is O(1) per operation on average, but inserting at the beginning shifts existing elements.
* The overall time complexity is O(n) in the worst case.
* The temporary list requires O(k) extra space, which is O(n) in the worst case.
* The method modifies the original list but also returns `nums`, whereas LeetCode expects in-place modification without relying on a return value.
"""

# Using pop() and a temporary list
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums:
            return
        k = k%len(nums)
        arr = []
        while k != 0:
            arr.append(nums.pop())
            k-=1
        nums[0:0] = arr[::-1]
        return nums


"""
Problem: 189. Rotate Array
Difficulty: Medium
Approach 2: Using Three Reversals

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Manipulation
* Two Pointers
* In-Place Reversal

Approach:

* Return immediately if `nums` is empty.
* Calculate `k = k % len(nums)`.
* Reverse the entire array using `self.reverse(nums, 0, len(nums) - 1)`.
* Reverse the first `k` elements using `self.reverse(nums, 0, k - 1)`.
* Reverse the remaining elements using `self.reverse(nums, k, len(nums) - 1)`.
* Implement the `reverse()` helper function using two pointers:
    * Swap the elements at `left` and `right`.
    * Increment `left` and decrement `right`.
    * Continue until `left >= right`.

Why it works:

* Reversing the entire array places the elements in reverse order.
* Reversing the first `k` elements restores the correct order of the elements moved to the beginning.
* Reversing the remaining elements restores the correct order of the other elements.
* The final result is a right rotation by `k` positions.

Limitation:

* The technique requires understanding how reversing different sections changes element order.
* It is important to handle `k = 0` correctly. The reversal operations still produce the original array in this case.
* The code must check whether `nums` is empty before calculating `k % len(nums)` to avoid division by zero.
"""

# Using three reversals for in-place rotation  
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k%len(nums)
        if not nums:
            return
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, left, right):
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            

"""
Problem: 189. Rotate Array
Difficulty: Medium
Approach 3: Using a Copy of the Original Array

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:

* Array Manipulation
* Index Mapping
* Auxiliary Array

Approach:

* Store the array length in `n`.
* Return immediately if `nums` is empty.
* Calculate `k = k % n`.
* Create a copy of the original array using `original = nums[:]`.
* Iterate through every index `i` from 0 to `n - 1`.
* Place each original element at its rotated index using `nums[(i + k) % n] = original[i]`.

Why it works:

* In a right rotation, an element originally at index `i` moves to index `(i + k) % n`.
* The modulo operator wraps indices around to the beginning when they exceed the last valid index.
* Reading from `original` ensures that overwriting `nums` does not destroy any values that are still needed.

Limitation:

* The copied array requires O(n) extra space.
* The approach is easy to understand but does not achieve the O(1) auxiliary-space requirement.
* The empty-array check must happen before any modulo operation involving `n`.
"""

# Using a copy and index mapping
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if not nums:
            return
        k %= n
        original = nums[:]
        for i in range(n):
            nums[(i+k)%n] = original[i]


"""
Problem: 189. Rotate Array
Difficulty: Medium
Approach 4: Using Python Slicing

Time Complexity: O(n)
Space Complexity: O(n)

Pattern:

* Array Manipulation
* Python Slicing
* In-Place Array Replacement

Approach:

* Store the array length in `n`.
* Return immediately if `nums` is empty.
* Calculate `k = k % n`.
* Split the array into two sections using slicing:
    * `nums[-k:]` selects the last `k` elements.
    * `nums[:-k]` selects all elements except the last `k`.
* Concatenate the sections in reverse order: `nums[-k:] + nums[:-k]`.
* Assign the result to `nums[:]` to replace the original list contents without changing the list object's identity.

Why it works:

* Right rotation moves the last `k` elements to the beginning.
* The remaining elements follow them in their original order.
* Python slicing and concatenation express this rearrangement directly.

Limitation:

* Slicing creates new lists, and concatenation creates another list.
* Therefore, the auxiliary space complexity is O(n).
* When `k = 0`, `nums[-k:]` becomes `nums[0:]`, which selects the entire list, while `nums[:-k]` becomes `nums[:0]`, which is empty. The result is still correct, but it is worth understanding this Python slicing behavior.
* The empty-array check must come before calculating `k % n`.
"""

# Using slicing to rearrange the array
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if not nums:
            return
        k %= n
        nums[:] = nums[-k:] + nums[:-k]


"""
Problem: 189. Rotate Array
Difficulty: Medium
Approach 5: Using Repeated pop() and insert()

Time Complexity: O(n * k), where k is the effective rotation count
Space Complexity: O(1) auxiliary space

Pattern:

* Array Manipulation
* Simulation
* In-Place Modification

Approach:

* Store the array length in `n`.
* Return immediately if `nums` is empty.
* Calculate `k = k % n`.
* Repeat the following operation `k` times:
    * Remove the last element using `nums.pop()`.
    * Insert that element at the beginning using `nums.insert(0, ...)`.

Why it works:

* Each iteration moves the last element to the first position.
* This performs one right rotation.
* Repeating the operation `k` times produces a right rotation by `k` positions.

Limitation:

* Inserting at index 0 shifts the other elements one position to the right.
* Each insertion can take O(n) time.
* Repeating the operation `k` times gives O(n * k) time complexity.
* Although the method uses O(1) auxiliary space, it can be inefficient when `k` is large.
"""

# Repeatedly moving the last element to the front
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if not nums:
            return
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())
            

"""
Problem: 189. Rotate Array
Difficulty: Medium
Approach 6: Using Cyclic Replacements

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:

* Array Manipulation
* Modular Arithmetic
* Cyclic Replacements
* In-Place Algorithms

Approach:

* Store the array length in `n`.
* Return immediately if `nums` is empty.
* Calculate `k = k % n`.
* Initialize `count = 0` to track the number of elements placed in their final positions.
* Initialize `start = 0` to identify the starting index of a cycle.
* While `count < n`:
    * Set `curr = start` and save the starting element in `prev = nums[start]`.
    * Calculate the next destination using `nxt = (curr + k) % n`.
    * Place `prev` at `nxt` while saving the overwritten value in `prev`:
        `nums[nxt], prev = prev, nums[nxt]`.
    * Update `curr = nxt` and increment `count`.
    * Stop the current cycle when `curr == start`.
    * Increment `start` to begin another cycle if elements remain unplaced.

Why it works:

* Each element moves to its correct destination using `(curr + k) % n`.
* The variable `prev` temporarily stores the element that must be placed next.
* Python evaluates the right-hand side of the assignment before assigning either target, so the overwritten value is saved safely.
* A cycle ends when the current index returns to its starting index.
* The `count` variable ensures every array element is moved exactly once, even when multiple cycles are needed.

Limitation:

* The implementation is more difficult to understand and debug than the reversal technique.
* Incorrect cycle termination or element-count tracking can cause infinite loops or incorrect results.
* When `k = 0`, every cycle contains just one index, so the algorithm leaves the array unchanged.

"""

# Using cyclic replacements to rotate in place    
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if not nums:
            return
        k %= n
        count = 0
        start = 0
        while count<n:
            curr = start
            prev = nums[start]

            while True:
                nxt = (curr+k)%n
                nums[nxt], prev = prev, nums[nxt]
                curr = nxt
                count += 1
                if curr == start:
                    break
            start += 1

