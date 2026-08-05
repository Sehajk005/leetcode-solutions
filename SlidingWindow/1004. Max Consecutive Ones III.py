"""
Brute Force Approach:
Generate All Subarrays

Problem: 1004. Max Consecutive Ones III

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(1)

Pattern:
Brute Force

Approach:
- Consider every possible starting index of a subarray.
- Extend the subarray one element at a time.
- Maintain the number of zeros in the current subarray.
- If the zero count is less than or equal to `k`, update the maximum length.
- Continue extending until all possible subarrays have been checked.

Key Insight:
- Every possible subarray is examined.
- Instead of recounting zeros for every subarray, keep a running zero count while extending the right boundary.
- This avoids the extra O(n) counting step and improves the naive O(n³) solution to O(n²).

Example:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Start at index 0:
[1]           -> 0 zeros ✓ Length = 1
[1,1]         -> 0 zeros ✓ Length = 2
[1,1,1]       -> 0 zeros ✓ Length = 3
[1,1,1,0]     -> 1 zero  ✓ Length = 4
[1,1,1,0,0]   -> 2 zeros ✓ Length = 5
[1,1,1,0,0,0] -> 3 zeros ✗

Repeat for every starting index.

Maximum Length = 6

Note:
- Every starting position is explored independently.
- The zero count is maintained while extending the subarray.
- No additional data structures are required.
- Although straightforward, checking every possible subarray makes this approach O(n²).
"""
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            zeroes = 0

            for j in range(i, n):
                if nums[j] == 0:
                    zeroes += 1

                if zeroes <= k:
                    max_len = max(max_len, j - i + 1)

        return max_len


"""
Optimal Approach:
Sliding Window

Problem: 1004. Max Consecutive Ones III

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Sliding Window

Approach:
- Maintain a window using two pointers (`left` and `right`).
- Expand the window by moving `right`.
- Count the number of zeros inside the current window.
- If the zero count exceeds `k`, shrink the window from the left until the window becomes valid again.
- Update the maximum window length after every valid expansion.

Key Insight:
- A window is valid as long as it contains at most `k` zeros.
- When the number of zeros becomes greater than `k`, only move the left pointer until one zero is removed.
- Since both pointers move forward only once, each element is processed at most twice.

Example:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Window Expansion:
[1]                 -> 0 zeros ✓ Length = 1
[1,1,1]             -> 0 zeros ✓ Length = 3
[1,1,1,0,0]         -> 2 zeros ✓ Length = 5
[1,1,1,0,0,0]       -> 3 zeros ✗

Shrink Window:
Move left until only 2 zeros remain.

Continue Expanding:
Eventually the largest valid window has length = 6.

Note:
- The window always contains at most `k` zeros.
- Each element enters the window once and leaves the window once.
- No extra arrays or data structures are used.
- This is the optimal solution because it processes the array in a single pass using O(1) extra space.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes-=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len
        
