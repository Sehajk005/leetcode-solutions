"""
Brute Force Approach:
Generate All Subarrays

Problem: 1493. Longest Subarray of 1's After Deleting One Element

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(1)

Pattern:
Brute Force

Approach:
- Consider every possible starting index of a subarray.
- Extend the subarray one element at a time.
- Maintain the number of zeros in the current subarray.
- Since we are allowed to delete exactly one element, the subarray can contain at most one zero.
- If the zero count is less than or equal to 1, update the answer.
- The length is calculated as (j - i) instead of (j - i + 1)
  because one element (the zero or one element if no zero exists) must be deleted.

Key Insight:
- Every possible subarray is examined.
- While extending the right boundary, keep a running zero count instead of
  recounting zeros each time.
- Using (j - i) automatically accounts for deleting one element.

Example:
nums = [1,1,0,1]

Start at index 0:
[1]         -> Delete one element → Length = 0
[1,1]       -> Delete one element → Length = 1
[1,1,0]     -> One zero ✓ Delete 0 → Length = 2
[1,1,0,1]   -> One zero ✓ Delete 0 → Length = 3

Repeat for every starting index.

Maximum Length = 3

Note:
- Every starting position is explored independently.
- At most one zero is allowed in the current subarray.
- No extra data structures are required.
- The solution is simple but checks all possible subarrays,
  resulting in O(n²) time.
"""
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            zeroes = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeroes += 1
                if zeroes <= 1:
                    max_len = max(max_len, j - i)
        return max_len
        
        
"""
Optimal Approach:
Sliding Window

Problem: 1493. Longest Subarray of 1's After Deleting One Element

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Sliding Window

Approach:
- Maintain a sliding window using two pointers.
- Count the number of zeros inside the current window.
- Expand the window by moving the right pointer.
- If the window contains more than one zero,
  shrink it from the left until only one zero remains.
- Since one element must always be deleted,
  the answer is (window size - 1),
  which is equivalent to (right - left).

Key Insight:
- The window always contains at most one zero.
- If there is one zero, deleting it connects all remaining ones.
- If there are no zeros, one element must still be deleted,
  so the answer is window length minus one.
- Every element enters and leaves the window at most once,
  giving O(n) time complexity.

Example:
nums = [1,1,0,1]

Expand Window:

Window = [1]
Zeros = 0
Length after deletion = 0

Window = [1,1]
Zeros = 0
Length after deletion = 1

Window = [1,1,0]
Zeros = 1
Length after deletion = 2

Window = [1,1,0,1]
Zeros = 1
Length after deletion = 3

Maximum Length = 3

Note:
- The window always satisfies the condition of having at most one zero.
- Shrink the window only when the zero count exceeds one.
- No extra data structures are used.
- Each element is processed at most twice,
  making the solution O(n).
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes = 0
        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes+=1
            while zeroes<=1:
                if nums[left] == 0:
                    zeroes-=1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len